# This is a subset of the session store example application presented in Chapter
# 18 of "The DynamoDB Book". Here, we want to delete all session tokens of a specific user.

import boto3
import time

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

results = table.query(
  TableName=table_name,
  IndexName='UserIndex',
  KeyConditionExpression="#username = :username",
  ExpressionAttributeNames={"#username": "Username"},
  ExpressionAttributeValues={":username": "adjutant" }
)

print(len(results['Items']))

batch = []
for res in results['Items']:
  req = {
    'DeleteRequest': {
      'Key': {
        'SessionToken': {'S': res['SessionToken']}
      }
    }
  }
  batch.append(req)
# END OF FOR LOOP #

start = time.perf_counter()

_ = client.batch_write_item(
  RequestItems = {
    'SessionStore': batch
  }
)

end = time.perf_counter()
secs = end - start
secs = round(secs, 3)
print(f"{secs}s")