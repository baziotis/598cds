import boto3
import time

dynamodb = boto3.resource('dynamodb')
table_name = 'BufTable'

# Create a new DynamoDB table with on-demand pricing
params = {
    'TableName': table_name,
    'KeySchema': [
        {'AttributeName': 'username',
         'KeyType': 'HASH' # i.e., partition key. We don't have a sort key.
        },
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'username', 'AttributeType': 'S'},
    ],
    'BillingMode': 'PAY_PER_REQUEST'
}

# Wait for the table to be created
table = dynamodb.create_table(**params)
print("Table was created")