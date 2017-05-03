'''
  For detailed information on API call, please checkout official boto3 website.
  => https://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Bucket.copy
  
  Please checkout my github for more information.
  => https://github.com/shawnkoon/aws_python_practice
  
  @purpose: Duplicate triggered object into specified output bucket.
  python v3.6
'''
import json
import boto3

# Using resource instead of client to reduce complexity.
s3 = boto3.resource('s3')

# This needs to changed to whichever output bucket the duplicated object will be stored.
destination_bucket_name = 'ewu.animationview.output'

def lambda_handler(event, context):
  # Print received object.
  print("Received event: " + json.dumps(event, indent=2))
  
  # Get Input bucket information along with the key.
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = event['Records'][0]['s3']['object']['key']
  
  # Source object template copy function will receive.
  copy_source = {
      'Bucket': bucket,
      'Key': key
  }
  try:
    dst_bucket = s3.Bucket(destination_bucket_name)
    print('=> Copy process begin : ' + key)
    copy_response = dst_bucket.copy(copy_source, key)
    print('=> Copy process to {} finished : '.format(destination_bucket_name) + key)
    return 'File Duplication Completed.'
  except Exception as e:
    print(e)
    raise e
