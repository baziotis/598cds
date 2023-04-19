# This is a subset of the session store example application presented in Chapter
# 18 of "The DynamoDB Book". Here, we want to delete all session tokens of a specific user.

import boto3
import time

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

start = time.perf_counter()

for result in results['Items']:
  table.delete_item(
    Key = {
      'SessionToken': result['SessionToken']
    }
  )
# END OF FOR LOOP #

end = time.perf_counter()
secs = end - start
secs = round(secs, 3)
print(f"{secs}s")