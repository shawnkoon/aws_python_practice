# Import
import boto3

tableName = 'exampleTable'
# Need to use resource because Table is under resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

# Prints creation time of the table
print('Creation Time : {0}\n'.format(table.creation_date_time))
# Print attribute definition of the table
print('Attribute Definition : {0}\n'.format(table.attribute_definitions))
# Prints Item count. Updates every 6hrs??? ...????
print('Total Item Count now = {0}\n'.format(table.item_count))

# Adds an Item to the Table
print('About to put(add) 5 itmes into Table [{0}]..\n'.format(tableName))
for count in range(0, 5):
  print('Adding id:{0} & username: shawnkoon_{1} ...'.format(count, count+1))
  table.put_item(
    Item={
      'id': count,
      'username': 'shawnkoon_{0}'.format(count + 1),
    },
  )

# Table Amazon Resource Name (ARN). (Unique ID for the table)
print('\nTable ARN = {0}\n'.format(table.table_arn))

# Prints table size in bytes. Updates every 6hrs??? ...????
print('Table [{0}] in Bytes = {1}'.format(tableName, table.table_size_bytes))

# Prints table status
print('Table [{0}] Status = {1}'.format(tableName, table.table_status))