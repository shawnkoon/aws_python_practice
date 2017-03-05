# Import
import boto3

# Create S3 client
s3_client = boto3.client('s3')

# bucket to inser item into
bucket_name = 'shawnkoon-example-bucket'

# Get all buckets
response = s3_client.list_buckets()
file = open('../files/test_file.txt','r+')

# Iterate through buckets to see if `bucket_name` exists
bucket_found = False
print("Finding to see if {} exists.".format(bucket_name))
for bucket in response['Buckets']:
	if bucket['Name'] == bucket_name:
		bucket_found = True

# bucket_found ? add item : exit
if bucket_found:
	print("Bucket {} found. Start adding an item...".format(bucket_name))
	response = s3_client.put_object(
		ACL='public-read',
		Bucket=bucket_name,
		Body=file,
		Key='test_file.txt'
	)
	print("Item was added to {} successfully.".format(bucket_name))
else:
	print("Bucket {} NOT found.. Exiting the program.".format(bucket_name))
