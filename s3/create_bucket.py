# Import
import boto3

# Create S3 client.
s3Client = boto3.client('s3')

# Create bucket with bucketName.
bucketName = 'shawnkoon-example-bucket'

print('Trying to create bucket named : [{0}]'.format(bucketName))
response = s3Client.create_bucket(
	Bucket=bucketName,
)
waiter = s3Client.get_waiter('bucket_exists')
waiter.wait(
  Bucket=bucketName
)
print('Response : {0}\n'.format(response))

# Printing list of buckets.
response = s3Client.list_buckets()
print('List of buckets : {0}\n'.format(response))
for bucket in response['Buckets']:
  print('Name : {0}'.format(bucket['Name']))
  print('Creation Date : {0}\n'.format(bucket['CreationDate']))


# Things I thought it was weird
# 1. I don't know if there is any way to tell if bucket already exists or not.
# 2. It doesn't throw exception when trying to create bucket that already exists. ( my acc buckets only )
