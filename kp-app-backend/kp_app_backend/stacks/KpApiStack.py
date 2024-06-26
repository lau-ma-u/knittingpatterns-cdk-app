from aws_cdk import (
    Stack,
    aws_apigateway as apigw_,
)
from constructs import Construct

class KpApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, integration: apigw_.LambdaIntegration, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a REST API.
        base_api = apigw_.RestApi(self, "PatternsApi", rest_api_name="PatternsApi")
        
        # Add resource with CORS.
        kp_entity = base_api.root.add_resource(
            'patterns',
            default_cors_preflight_options=apigw_.CorsOptions(
                allow_methods=apigw_.Cors.ALL_METHODS,
                allow_origins=apigw_.Cors.ALL_ORIGINS)
        )

        # Add methods to the resource.
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

        kp_entity.add_method(
            'POST', integration,
            method_responses=[
                apigw_.MethodResponse(
                    status_code="200",
                    response_parameters={
                        'method.response.header.Access-Control-Allow-Origin': True
                    }
                )
            ]
        )