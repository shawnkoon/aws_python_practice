# Source : https://github.com/shawnkoon

import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

response = client.list_tables()

print('\nPrinting response : type - ' + str(type(response)))
print(str(response) + '\n')

print('Printing each Table names : ')
for table in response['TableNames']:
	print(table)

print('\n')
print('Scanning values of each Tables : ')
for table in response['TableNames']:
	scan_result = client.scan(TableName=table)
	print(scan_result)
	print('Item Coutn : {0}'.format(dynamodb.Table(table).item_count))

	for item in scan_result['Items']:
		print()
		print(item)

		for key, value in item.items():
			print('key = ' + key + ', value = ' + str(value))
	print()

print('\n\nDone.')

# ------ Things I learned -------
# boto3.clinet('dynamodb') to access all dynamodb related functions.
# Use items() to access all data in dict
# DynamoDB is sorted with Partition key first, then Sort Key.
# scan() returns all items related to that Table.
