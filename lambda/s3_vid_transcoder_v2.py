'''
Version : 2.
Change  : Added get_prefix() to apply same prefix for the
          Output file.
This lambda function will get triggered by
S3 PUT events with input videos of certain extension
http://boto3.readthedocs.io/en/latest/reference/services/elastictranscoder.html#ElasticTranscoder.Client.create_job

Please checkout my github for more information.
=> https://github.com/shawnkoon/aws_python_practice
'''
from __future__ import print_function

import json
import boto3

client = boto3.client('elastictranscoder')

def get_base_name(full_path):
	return full_path.split('/')[-1].split('.')[0]

def get_output_key(key, ext):
	return 'tc_' + key + '.' + ext
	
def get_prefix(path):
	split_array = path.split('/')
	return '/'.join(split_array[0:len(split_array) - 1]) + '/'

def lambda_handler(event, context):
	# Print received object.
	print("Received event: " + json.dumps(event, indent=2))

	# Get key value of S3 object.
	key = event['Records'][0]['s3']['object']['key']

	# Set the Transcoder param values.
	pipeline_id = '1492657799851-cnb8gl'

	# Retrieve prefix of the object that was created.
	output_key_prefix = get_prefix(key)

	# Generic 720p
	preset_id = '1351620000001-000010' 

	# Input params.
	params = {
		'PipelineId' : pipeline_id,
		'OutputKeyPrefix' : output_key_prefix,
		'Input' : {
			'Key' : key
		},
		'Output' : {
			'Key' : get_output_key(get_base_name(key), 'mp4'),
			'PresetId' : preset_id
		}
	}

	try:
		# Creates a job with specified kwargs.
		# Only problem is that it does not recognize Job failure.
		# Might need to add SNS topic to elastic transcoder with lambda Trigger.
		transcode_response = client.create_job(**params)
		return transcode_response['ResponseMetadata']
	except Exception as e:
		print(e)
		print('Error!!')
		raise e