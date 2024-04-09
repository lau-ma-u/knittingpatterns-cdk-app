from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb_,
    aws_lambda as lambda_,
    aws_apigateway as apigw_,
    aws_s3 as s3,

)
from constructs import Construct
import os.path

class KpApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, integration: apigw_.LambdaIntegration, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        base_api = apigw_.apigateway.RestApi(self, "PatternsApi", rest_api_name="PatternsApi")
        
        kp_entity = base_api.root.add_resource(
            'example',
            default_cors_preflight_options=apigw_.CorsOptions(
                allow_methods=apigw_.Cors.ALL_METHODS,
                allow_origins=apigw_.Cors.ALL_ORIGINS)
        )

        kp_entity.add_method(
            'GET', integration,
            method_responses=[
                apigw_.MethodResponse(
                    status_code="200",
                    response_parameters={
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )