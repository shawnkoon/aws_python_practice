# Import
import boto3

tableName = 'exampleTable'
# Need to use resource to access Table obj
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

# Get one particular item from the table.
print('About to fetch item with id = 1 from [{0}] table'.format(tableName))
try:
  response = table.get_item(
    Key={
      'id': 0,
    },
  )
  item = response['Item']
  print('Item with id 1 has username : [{0}]'.format(item['username']))
except Exception as e:
  print(e)
  print('Please try again later.. might be an adding delay.')
