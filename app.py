#!/usr/bin/env python3

from aws_cdk import core

from cdk_sample.cdk_sample_stack import CdkSampleStack

# with open('config/env_lower.yaml') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)


app = core.App()
CdkSampleStack(app, "cdk-sample")

app.synth()
