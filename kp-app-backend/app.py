#!/usr/bin/env python3
import os

import aws_cdk as cdk

from kp_app_backend.stacks.KpDataStack import KpDataStack
from kp_app_backend.stacks.KpLambdasStack import KpLambdasStack

app = cdk.App()
data_stack = KpDataStack(app, "KpDataStack")
lambda_stack = KpLambdasStack(app, 'KpLambdaStack', data_stack.patterns_table)


app.synth()
