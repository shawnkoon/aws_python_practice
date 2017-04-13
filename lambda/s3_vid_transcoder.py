'''
This lambda function will get triggered by
S3 PUT events with input videos of certain extension
'''
from __future__ import print_function

import json
import boto3

client = boto3.client('elastictranscoder')

def lambda_handler(event, context):
	pass