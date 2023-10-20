from churn.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from churn.entity.artifact_entity import DataIngestionArtifact
from churn.components.data_ingestion import DataIngestion
from churn.exception import ChurnException
from churn.logger import logging
import os,sys

class TrainPipeline:
    def __init__(self) :
        training_pipeline_config = TrainingPipelineConfig()
        self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed")

            return data_ingestion_artifact
        except Exception as e:
            raise ChurnException(e,sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise ChurnException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise ChurnException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise ChurnException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise ChurnException(e,sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise ChurnException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact =self.start_data_ingestion()
        except Exception as e:
            raise ChurnException(e,sys)
