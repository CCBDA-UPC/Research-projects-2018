import base64
import boto3
import datetime
import os
import random
import sys
import time
from urllib.parse import urlparse

# The URL of the sample data in S3
UNSCORED_DATA_S3_URL = "s3://sample-bucket/banking-batch.csv"


def use_model(model_id, threshold, ds_id):

    ml = boto3.client('machinelearning')

    ml.update_ml_model(MLModelId=model_id, ScoreThreshold=threshold)

    bp_id = 'bp-' + base64.b32encode(os.urandom(10)).decode()
    ml.create_batch_prediction(
        BatchPredictionId=bp_id,
        BatchPredictionName="Batch Prediction for marketing sample",
        MLModelId=model_id,
        BatchPredictionDataSourceId=ds_id,
        OutputUri="s3://ccbda-upc-rui/output"
    )
    print("Batch prediction created")

# Check model status, wait until it's finished
def poll_until_completed(model_id):

    ml = boto3.client("machinelearning")
    delay = 2
    while True:
        model = ml.get_ml_model(MLModelId=model_id)
        status = model['Status']
        if status in ['COMPLETED', 'FAILED', 'INVALID']:
            break
        delay *= random.uniform(1.1, 2.0)
        time.sleep(delay)


def create_data_sources(data_s3url, input_data):

    ml = boto3.client("machinelearning")
    ds_id = 'ds-' + base64.b32encode(os.urandom(10)).decode()

    ml.create_data_source_from_s3(
        DataSourceId=ds_id,
        DataSourceName="batch_prediction",
        DataSpec={
            "DataLocationS3": data_s3url,
            "DataSchema": open(input_data).read(),
        },
        ComputeStatistics=False
    )
    print("Batch datasource created")
    return ds_id

ds_id = create_data_sources(UNSCORED_DATA_S3_URL,"banking-batch.csv.schema")
poll_until_completed("ml-W7U36YMOGZBZAMF3")
use_model("ml-W7U36YMOGZBZAMF3", 0.7, ds_id)