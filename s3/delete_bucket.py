# Import
import boto3

# Create S3 client.
s3_client = boto3.client('s3')

# Create bucket name desired to be deleted.
bucket_name = 'shawnkoon-example-bucket'

# Get all buckets.
response = s3_client.list_buckets()

# Iterate through buckets to see if `bucket_name` exists
bucket_found = False
print("Finding to see if {} exists.".format(bucket_name))
for bucket in response['Buckets']:
	if bucket['Name'] == bucket_name:
		bucket_found = True

# Bucket found? delete : exit
if bucket_found:
	print("Bucket {} found. Start Deleting...".format(bucket_name))
	response = s3_client.delete_bucket(
		Bucket=bucket_name
	)
	print("Bucket {} successfully deleted! :)".format(bucket_name))
else:
	print("Bucket {} NOT found.. Exiting the program.".format(bucket_name))


# Make sure empty the bucket before deleting.
# Possible change.

# for key in bucket.objects.all():
#		key.delete()
# bucket.delete()

# Another side tip.
# -> Deleting all buckets with all data. (bucket nuking? :troll:)

# for bucket in s3.buckets.all():
#		for key in bucket.objeccts.all():
#			key.delete()
#		bucket.delete()

# Use at your own risk :)
