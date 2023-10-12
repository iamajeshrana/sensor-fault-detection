# Compulsory this library or code import all project
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlproject" # this name mention as your wish don't required any where its just for this module project package 

list_of_files = [
    ".github/workflows/main.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/cloud_storage/__init__.py",
    f"src/{project_name}/cloud_storage/s3_syncer.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/mongo_db_connection.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/application.py",
    f"src/{project_name}/constant/database.py",
    f"src/{project_name}/constant/env_variable.py",
    f"src/{project_name}/constant/s3_bucket.py",
    f"src/{project_name}/constant/training_pipeline/__init__.py",
    f"src/{project_name}/data_access/__init__.py",
    f"src/{project_name}/data_access/sensor_data.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/metric/__init__.py",
    f"src/{project_name}/ml/metric/classification_metric.py",
    f"src/{project_name}/ml/metric/__init__.py",
    f"src/{project_name}/ml/model/estimator.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/main_utils.py",
    "config/schema.yaml",
    "report.yaml",
    "main.py", # this code have new additions, but this file you have created manually project
    "Dockerfile", # this code have new additions, but this file you have created manually project
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    
]


for filepath in list_of_files:
    # Sometimes getting a issue for backslashes because normally computer use the forward slashes so that above file use / forward slashes, below code help
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")