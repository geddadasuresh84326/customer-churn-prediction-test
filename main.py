from churn.exception import ChurnException
from churn.logger import logging
import os
import sys
import pandas as pd
from churn.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from churn.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    try:
        # logging.info("division operation")
        # a = 1/0
        # df = pd.read_excel("customer_churn_large_dataset.xlsx")
        # logging.info(f"Reading the data completed : {df.shape}")
        traine_pipeline = TrainPipeline()
        traine_pipeline.run_pipeline()

    except Exception as e:
        logging.info(f"error occurred :{e}")
        raise ChurnException(e,sys)