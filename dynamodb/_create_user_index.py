#### YOU DON'T NEED TO USE THIS ####

import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')
table_name = 'SessionStore'

index_name = 'UserIndex'
partition_key = 'Username'

# Define the attributes to project from the table into the index
projection_attributes = ['SessionToken']

# Define the GSI key schema
key_schema = [
    {
        'AttributeName': partition_key,
        'KeyType': 'HASH'
    }
]

# Create the GSI
response = dynamodb.update_table(
    TableName=table_name,
    BillingMode='PAY_PER_REQUEST',
    AttributeDefinitions=[
        {
            'AttributeName': partition_key,
            'AttributeType': 'S'
        }
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': index_name,
                'KeySchema': key_schema,
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': projection_attributes
                },
            }
        }
    ]
)

# Print the response
print(response)