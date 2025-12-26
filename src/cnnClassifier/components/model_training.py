import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
import math
import json
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    @staticmethod
    def save_history(path: Path, history: dict):
        path.parent.mkdir(parents=True, exist_ok=True)
    
        # Convert numpy types to native Python types
        cleaned_history = {
            key: [float(value) for value in values]
            for key, values in history.items()
        }
    
        with open(path, "w") as f:
            json.dump(cleaned_history, f, indent=4)

    
    def get_callbacks(self):
        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        )

        reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.2,
            patience=3,
            min_lr=1e-6
        )
        
        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.trained_model_path,
            monitor="val_loss",
            save_best_only=True
        )
        
        return [early_stopping, reduce_lr, checkpoint]

    
    def train(self):
        self.steps_per_epoch = math.ceil(
        self.train_generator.samples / self.train_generator.batch_size
        )
        self.validation_steps = math.ceil(
            self.valid_generator.samples / self.valid_generator.batch_size
        )
        callbacks = self.get_callbacks()

        history = self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,  # upper bound only
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps,
            callbacks=callbacks
        )    

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

        self.save_history(
            path=self.config.history_path,
            history=history.history
        )