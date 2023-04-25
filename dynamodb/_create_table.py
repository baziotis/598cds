import boto3
import time

dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'

# Create a new DynamoDB table with on-demand pricing
params = {
    'TableName': table_name,
    'KeySchema': [
        {'AttributeName': 'SessionToken',
         'KeyType': 'HASH' # i.e., partition key. We don't have a sort key.
        },
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'SessionToken', 'AttributeType': 'S'},
    ],
    'BillingMode': 'PAY_PER_REQUEST'
}

# Wait for the table to be created
table = dynamodb.create_table(**params)
print("Table was created")