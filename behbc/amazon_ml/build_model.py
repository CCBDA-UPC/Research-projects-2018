import base64
import boto3
import json
import os

TRAINING_DATA_S3_URL = "s3://sample-bucket/banking.csv"

def create_data_sources(data_s3_url, input_data, train_percent=70):

    ml = boto3.client("machinelearning")
    train_ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()
    spec = {
        "DataLocationS3": data_s3_url,
        "DataRearrangement": json.dumps({
            "splitting": {
                "percentBegin": 0,
                "percentEnd": train_percent
            }
        }),
        "DataSchema": open(input_data).read(),
    }

    ml.create_data_source_from_s3(
        DataSourceId = train_ds_id,
        DataSpec=spec,
        DataSourceName="training",
        ComputeStatistics=True
    )
    print("Training data set created\n")

    test_ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()

    spec ={
        "DataLocationS3": data_s3_url,
        "DataRearrangement": json.dumps({
            "splitting":{
                "percentBegin": train_percent,
                "percentEnd":100
            }
        }),
        "DataSchema": open(input_data).read(),
    }

    ml.create_data_source_from_s3(
        DataSourceId=test_ds_id,
        DataSpec=spec,
        DataSourceName="testing",
        ComputeStatistics=True
    )
    print("Test data set created\n")
    return (train_ds_id,test_ds_id)

def create_model(train_id, recipe):

    ml = boto3.client("machinelearning")
    model_id = 'ml-' + base64.b32encode(os.urandom(10)).decode()
    ml.create_ml_model(
        MLModelId=model_id,
        MLModelName="first_model",
        MLModelType="BINARY",  # we're predicting True/False values
        Parameters={
            # Refer to the "Machine Learning Concepts" documentation
            # for guidelines on tuning your model
            "sgd.maxPasses": "100",
            "sgd.maxMLModelSizeInBytes": "104857600",  # 100 MiB
        },
        Recipe=open(recipe).read(),
        TrainingDataSourceId=train_id
    )
    print("ML Model created")
    return model_id

def create_evaluation(model_id, test_id):
    ml = boto3.client("machinelearning")
    eval_id = 'eval-' + base64.b32encode(os.urandom(10)).decode()
    ml.create_evaluation(
        EvaluationId=eval_id,
        EvaluationName="evaluation",
        MLModelId=model_id,
        EvaluationDataSourceId=test_id
    )
    print("Evaluation created")
    return eval_id

(train_ds_id,test_ds_id) = create_data_sources(TRAINING_DATA_S3_URL, "banking.csv.schema")
model_id = create_model(train_ds_id,"recipe.json")
eval_id = create_evaluation(model_id,test_ds_id)