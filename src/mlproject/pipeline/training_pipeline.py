# from src.mlproject.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
# from src.mlproject.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact,DataTransformationArtifact
# from src.mlproject.entity.artifact_entity import ModelEvaluationArtifact,ModelPusherArtifact,ModelTrainerArtifact
# from src.mlproject.entity.config_entity import ModelPusherConfig,ModelEvaluationConfig,ModelTrainerConfig
# from src.mlproject.exception import CustomException
# import sys,os
# from src.mlproject.logger import logging
# from src.mlproject.components.data_ingestion import DataIngestion
# from src.mlproject.components.data_validation import DataValidation
# from src.mlproject.components.data_transformation import DataTransformation
# from src.mlproject.components.model_trainer import ModelTrainer
# from src.mlproject.components.model_evaluation import ModelEvaluation
# from src.mlproject.components.model_pusher import ModelPusher
# from src.mlproject.constant.training_pipeline import SAVED_MODEL_DIR

# class TrainPipeline:
#     is_pipeline_running=False # This code have used after model pusher.
#     def __init__(self):
#         self.training_pipeline_config = TrainingPipelineConfig()
       

#     def start_data_ingestion(self)->DataIngestionArtifact:
#         try:
#             self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
#             logging.info("Starting data ingestion")
#             data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
#             data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
#             logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
#             return data_ingestion_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)

#     def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
#         try:
#             data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
#             data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
#             data_validation_config = data_validation_config
#             )
#             data_validation_artifact = data_validation.initiate_data_validation()
#             return data_validation_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)

#     def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
#         try:
#             data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
#             data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
#             data_transformation_config=data_transformation_config
#             )
#             data_transformation_artifact =  data_transformation.initiate_data_transformation()
#             return data_transformation_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)
    
#     def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact):
#         try:
#             model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
#             model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
#             model_trainer_artifact = model_trainer.initiate_model_trainer()
#             return model_trainer_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)

#     def start_model_evaluation(self,data_validation_artifact:DataValidationArtifact,
#                                  model_trainer_artifact:ModelTrainerArtifact,
#                                 ):
#         try:
#             model_eval_config = ModelEvaluationConfig(self.training_pipeline_config)
#             model_eval = ModelEvaluation(model_eval_config, data_validation_artifact, model_trainer_artifact)
#             model_eval_artifact = model_eval.initiate_model_evaluation()
#             return model_eval_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)

#     def start_model_pusher(self,model_eval_artifact:ModelEvaluationArtifact):
#         try:
#             model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
#             model_pusher = ModelPusher(model_pusher_config, model_eval_artifact)
#             model_pusher_artifact = model_pusher.initiate_model_pusher()
#             return model_pusher_artifact
#         except  Exception as e:
#             raise  CustomException(e,sys)

#     def run_pipeline(self):
#         try:
            
#             TrainPipeline.is_pipeline_running=True # This code is used for after model pusher if pipeline running show show true

#             data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
#             data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)
#             data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
#             model_trainer_artifact = self.start_model_trainer(data_transformation_artifact)
#             model_eval_artifact = self.start_model_evaluation(data_validation_artifact, model_trainer_artifact)
#             if not model_eval_artifact.is_model_accepted:
#                 raise Exception("Trained model is not better than the best model")
#             model_pusher_artifact = self.start_model_pusher(model_eval_artifact)
#             TrainPipeline.is_pipeline_running=False # This code have used after the model false if pipeline not running show false
#         except  Exception as e:
#             raise  CustomException(e,sys)
        


###########################################################################################################################
######################Above code have used for Till Model Pusher with Main.py Server testing purpose#######################
# Ensure if you have locally testing for backend server working or not then you can not give any s3 bucket details in training pipeline
# If you have store all the artificates and saved_model in s3 bucket then you can do add all code constant, s3_sycer code, training pipleline code you have add, run python main.py you check all details store in cloud s3 bucket
# After done all this then you can docker image create, deployment process with CI/CD Pipeline 
###########################################################################################################################


from src.mlproject.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from src.mlproject.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact,DataTransformationArtifact
from src.mlproject.entity.artifact_entity import ModelEvaluationArtifact,ModelPusherArtifact,ModelTrainerArtifact
from src.mlproject.entity.config_entity import ModelPusherConfig,ModelEvaluationConfig,ModelTrainerConfig
from src.mlproject.exception import CustomException
import sys,os
from src.mlproject.logger import logging
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_validation import DataValidation
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer
from src.mlproject.components.model_evaluation import ModelEvaluation
from src.mlproject.components.model_pusher import ModelPusher
from src.mlproject.cloud_storage.s3_syncer import S3Sync  # Only this code add 
from src.mlproject.constant.s3_bucket import TRAINING_BUCKET_NAME # Only this code add 
from src.mlproject.constant.training_pipeline import SAVED_MODEL_DIR

class TrainPipeline:
    is_pipeline_running=False # This code have used after model pusher.
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.s3_sync = S3Sync() # this code add
        


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  CustomException(e,sys)

    def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except  Exception as e:
            raise  CustomException(e,sys)

    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
            data_transformation_config=data_transformation_config
            )
            data_transformation_artifact =  data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except  Exception as e:
            raise  CustomException(e,sys)
    
    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact):
        try:
            model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except  Exception as e:
            raise  CustomException(e,sys)

    def start_model_evaluation(self,data_validation_artifact:DataValidationArtifact,
                                 model_trainer_artifact:ModelTrainerArtifact,
                                ):
        try:
            model_eval_config = ModelEvaluationConfig(self.training_pipeline_config)
            model_eval = ModelEvaluation(model_eval_config, data_validation_artifact, model_trainer_artifact)
            model_eval_artifact = model_eval.initiate_model_evaluation()
            return model_eval_artifact
        except  Exception as e:
            raise  CustomException(e,sys)

    def start_model_pusher(self,model_eval_artifact:ModelEvaluationArtifact):
        try:
            model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
            model_pusher = ModelPusher(model_pusher_config, model_eval_artifact)
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except  Exception as e:
            raise  CustomException(e,sys)
        
    #     # below code add for s3

    def sync_artifact_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder = self.training_pipeline_config.artifact_dir,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise CustomException(e,sys)
            
    def sync_saved_model_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/{SAVED_MODEL_DIR}"
            self.s3_sync.sync_folder_to_s3(folder = SAVED_MODEL_DIR,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise CustomException(e,sys)

    def run_pipeline(self):
        try:
            
            TrainPipeline.is_pipeline_running=True # This code is used for after model pusher if pipeline running show show true

            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact)
            model_eval_artifact = self.start_model_evaluation(data_validation_artifact, model_trainer_artifact)
            if not model_eval_artifact.is_model_accepted:
                raise Exception("Trained model is not better than the best model")
            model_pusher_artifact = self.start_model_pusher(model_eval_artifact)
            TrainPipeline.is_pipeline_running=False # This code have used after the model false if pipeline not running show false
            self.sync_artifact_dir_to_s3() # this code add
            self.sync_saved_model_dir_to_s3() # this code add
        except  Exception as e:
            self.sync_artifact_dir_to_s3() # this code add
            TrainPipeline.is_pipeline_running=False # This code we have used after the model false if pipeline not running show false
            raise  CustomException(e,sys)