import numpy as np
import tensorflow as tf
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model ONCE per request (we'll optimize later)
        model = tf.keras.models.load_model(
            os.path.join("model", "trained_model.h5") # made new directory for model files as we do not passed artifact folder so it will throw error of file not found
        )

        # Load and preprocess image (CORRECT API)
        test_image = tf.keras.utils.load_img(
            self.filename,
            target_size=(224, 224)
        )
        test_image = tf.keras.utils.img_to_array(test_image)
        test_image = test_image / 255.0  # IMPORTANT (matches training)
        test_image = np.expand_dims(test_image, axis=0)

        # Prediction
        prediction_probs = model.predict(test_image)
        result = np.argmax(prediction_probs, axis=1)

        if result[0] == 1:
            return [{"image": "Tumor"}]
        else:
            return [{"image": "Normal"}]
