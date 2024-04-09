import boto3
import os
import json
import logging
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb_client = boto3.client("dynamodb")

def handler(event, context):
    table = os.environ.get("TABLE_NAME")
    logging.info(f"## Loaded table name from environemt variable DDB_TABLE: {table}")
    logging.info(event)
    if event["body"]:
        item = json.loads(event["body"])
        logging.info(f"## Received payload: {item}")
        title = str(item["title"])
        yarn = str(item["yarn"])
        amount = str(item["amount"])
        needle_size = str(item["needle_size"])

        # id = str(item["id"])
        dynamodb_client.put_item(
            TableName=table,
            Item={"title": {"S": title}, "yarn": {"S": yarn}, "amount": {"S": amount}, "needle_size": {"S": needle_size}, "id": {"S": str(uuid.uuid4())}},
        )
        message = "Successfully inserted data!"
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": message}),
        }
    else:
        logging.info("## Received request without a payload")
        """ dynamodb_client.put_item(
            TableName=table,
            Item={
                "year": {"N": "2012"},
                "title": {"S": "The Amazing Spider-Man 2"},
                "id": {"S": str(uuid.uuid4())},
            },
        )
        message = "Successfully inserted data!" """
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": message}),
        }