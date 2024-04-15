import boto3
import os
import json
import logging
import uuid

dynamodb_client = boto3.client("dynamodb")

def handler(event, context):

    table = os.environ.get("TABLE_NAME")

     # Handler implementation will be added later