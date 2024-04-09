from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb_,
    aws_lambda as lambda_,
)
from constructs import Construct
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk
import os.path

TABLE_NAME = "patterns_table"

class KpAppBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDb Table
        demo_table = dynamodb_.Table(
            self,
            TABLE_NAME,
            partition_key=dynamodb_.Attribute(
                name="id", type=dynamodb_.AttributeType.STRING
            ),
        )

        # Create S3 bucket for storing image files.
        bucket = s3.Bucket(self, "ImagesBucket", versioned=True, auto_delete_objects=True, removal_policy=cdk.RemovalPolicy.DESTROY)
