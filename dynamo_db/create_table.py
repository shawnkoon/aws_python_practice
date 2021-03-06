# Imports.
import boto3

# Get the service client from AWS (dynamodb)
dynamodb = boto3.client('dynamodb')
# dynamodb = boto3.resource('dynamodb')

tableName = 'exampleTable'

# Create new dynamodb table
newTable = dynamodb.create_table(
	TableName=tableName,
	KeySchema=[
		{
			'AttributeName': 'id',
			'KeyType': 'HASH',
		},
		{
			'AttributeName': 'username',
			'KeyType': 'RANGE',
		},
	],
	AttributeDefinitions=[
		{
			'AttributeName': 'id',
			'AttributeType': 'N',
		},
		{
			'AttributeName': 'username',
			'AttributeType': 'S',
		},
	],
	ProvisionedThroughput={
		'ReadCapacityUnits': 5,
		'WriteCapacityUnits': 5,
	},
)

print('Creating table {0}....'.format(tableName))

# Wait Until the finishes creating using waiter.
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(
	TableName=tableName,
)

print('Table {0} creation completed!\nBye.'.format(tableName))

# This creates a table named users that respectively has the hash and range primary keys id and username.
# This method will return a DynamoDB.Table resource to call additional methods on the created table.
# src : https://boto3.readthedocs.io/en/latest/guide/dynamodb.html#creating-a-new-table

# Things I found.
# 1. boto3.resource && boto3.client are similar but client offers more features.
# 2. Thre are 4 required attributes in create_table call.
# 	a. TableName. - desired table name.
#		b. AttributeDefinitions. - define each key schemas.
#			1. AttributeName
#			2. AttributeType (S || N || B)
#		c. KeySchema. - schema to determine HASH(partition) key && RANGE(sort) keys.
#			1. AttributeName
#			2. KeyType
#		d. ProvisionedThroughput. - define read/write cpacity unit.
#			1. ReadCapacityUnits
#			2. WriteCapacityUnits
#		- https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.create_table
# 3. [] = list / {} = dict
# 4. get_waiter only works with client.
# 5. get_waiter has 2 different types.
# 	a. 'table_exists'
#		b. 'table_not_exists'
