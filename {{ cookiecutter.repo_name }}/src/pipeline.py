import shutil
import pandas as pd
import tempfile
from sbml.pipeline_builder import *
from data.data_access import get_data
from features.build_features import build_features
from models.train_model import train_model


@metadata
def metadata():
    #Example: return {'project_name': 'The_First'}


@data_ingestion
def ingest_data():
    # Example: return pd.read_csv("snowflake/training_data_for_lead_scoring.csv")


@data_validation
def validate_data(training_data):
    #Excample: return not training_data.empty


@feature_engineering
def feature_engineering(training_data):
    #Example: return training_data[['household_sessions', 'minutes_between_se_start_and_rfq']]


@model_training
def model_training(features):
    #Example: return training_data[['household_sessions', 'minutes_between_se_start_and_rfq']]


@model_evaluation
def model_evaluation(model):
    #Example: Check the model gives the accepted values for metrics



@model_deployment
def model_deployment(model):
    #Example: Create a Sagemaker ednpoint?


@model_monitoring
def model_monitoring():
    #Example: setup some extra monitoring


if __name__ == '__main__':
    run_pipeline()