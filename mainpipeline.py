from src.mlproject.configuration.mongo_db_connection import MongoDBClient 
from src.mlproject.exception import CustomException
import os,sys
from src.mlproject.logger import logging
from src.mlproject.pipeline import training_pipeline
from src.mlproject.pipeline.training_pipeline import TrainPipeline
from src.mlproject.utils.main_utils import read_yaml_file
# Ajeshg

if __name__=='__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
        mongodb_client=MongoDBClient()
        print(mongodb_client.database.list_collection_names())

    except Exception as e:
        print(e)
        logging.exception(e)