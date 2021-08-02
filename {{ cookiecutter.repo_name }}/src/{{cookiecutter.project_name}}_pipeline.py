import shutil
import pandas as pd
import tempfile
from sbml.pipelines.pipeline_builder import Pipeline
from data.data_access import get_data
from features.build_features import build_features
from models.train_model import train_model


pipeline = Pipeline(name="{{cookiecutter.project_name}}")

@pipeline.data_ingestion
def ingest_data() -> Dict:
    data = get_data()
    # Example: return pd.read_csv("snowflake/training_data_for_lead_scoring.csv")
    return {}


@pipeline.data_validation
def validate_data(training_data) -> bool:
    #Excample: return not training_data.empty
    return True


@pipeline.feature_engineering
def feature_engineering(training_data) -> Dict:
    features = build_features()
    #Example: return training_data[['household_sessions', 'minutes_between_se_start_and_rfq']]
    return {"features": "xxxxxx"}


@pipeline.training
def model_training(features) -> Dict:
    #Example: return training_data[['household_sessions', 'minutes_between_se_start_and_rfq']]
    return {"model": "xxxxx"}


@pipeline.model_testing
def model_testing(model) -> Dict:
    #Example: Check the model gives the accepted values for metrics
    return {}


@pipeline.model_deployment
def model_deployment(model) -> Dict:
    #Example: Create a Sagemaker ednpoint?
    return {}


if __name__ == '__main__':
    pipeline.run()
