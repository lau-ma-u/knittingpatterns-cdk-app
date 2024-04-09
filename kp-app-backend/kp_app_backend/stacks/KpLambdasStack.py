from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb_,
    aws_lambda as lambda_,
    aws_apigateway as apigw_
)
from constructs import Construct
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk
import os.path

dirname = os.path.dirname(__file__)

class KpLambdasStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, table: dynamodb_, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the Lambda function to receive the request
        api_handler = lambda_.Function(
            self,
            "ApiHandler",
            function_name="kp_api_handler",
            runtime=lambda_.Runtime.PYTHON_3_11,
            code=lambda_.Code.from_asset(os.path.join(dirname, "../lambdas")),
            handler="kp-api-handler.handler",
            
        )
        
        # grant permission to lambda to write to patterns table
        table.grant_write_data(api_handler)
        api_handler.add_environment("TABLE_NAME", table.table_name)

        self.lambda_integration = apigw_.LambdaIntegration(api_handler)