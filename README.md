# 🩺 Kidney Disease Classification using Deep Learning

An end-to-end Deep Learning project for **classifying kidney diseases from CT scan images**.
The model predicts one of the following classes:

- **Cyst**
- **Tumor**
- **Stone**
- **Normal**

This project is designed with **research, reproducibility, and deployment** in mind.

---

## 📌 Project Overview

Early detection of kidney diseases is critical for effective treatment.
This project uses **Transfer Learning with CNN architectures** to automate kidney disease classification from CT scans.

The pipeline is structured to be **production-ready**, scalable, and easy to extend.

---

## ✨ Key Features

- 🔹 **Deep Learning–based CT Scan Classification**
- 🔹 **Transfer Learning (EfficientNet / CNN-based models)**
- 🔹 **Modular & Clean Codebase**
- 🔹 **MLflow Integration** for experiment tracking
- 🔹 **DVC** for dataset version control
- 🔹 **Flask Web App** for predictions
- 🔹 **Docker-ready** for deployment
- 🔹 **CI/CD friendly** (GitHub Actions compatible)

---

## 🏗️ Tech Stack

| Category | Tools |
|--------|------|
| Language | Python 3.8+ |
| Deep Learning | TensorFlow, Keras |
| Data Handling | NumPy, Pandas |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Web Framework | Flask |
| Visualization | Matplotlib, Seaborn |
| Deployment | Docker |

---
 

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Indrayani-B/KidneyScan 
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.9 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






<!-- ## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app -->



