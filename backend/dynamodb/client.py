import os

import boto3
from dotenv import load_dotenv

load_dotenv()

IS_LOCAL = os.environ.get("USE_LOCAL_DYNAMO", "false").lower() == "true"

if IS_LOCAL:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="ap-northeast-1",
        endpoint_url="http://localhost:8001",
        aws_access_key_id="dummy",
        aws_secret_access_key="dummy",
    )
else:
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="ap-northeast-1",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )
