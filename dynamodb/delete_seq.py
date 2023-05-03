# This is a subset of the session store example application presented in Chapter
# 18 of "The DynamoDB Book". Here, we want to delete all session tokens of a specific user.

import boto3
from boto3.dynamodb.conditions import Attr
import time
import delete_config

dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

results = table.scan(
  FilterExpression=Attr('Username').eq(delete_config.user)
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