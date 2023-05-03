# This is a subset of the session store example application presented in Chapter
# 18 of "The DynamoDB Book". Here, we want to delete all session tokens of a specific user.

import boto3
from boto3.dynamodb.conditions import Attr
import time
import delete_config

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

results = table.scan(
  FilterExpression=Attr('Username').eq(delete_config.user)
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

MAXIMUM_NUM_OF_REQUESTS_PER_BATCH = 25
smaller_batches = []

start = time.perf_counter()

step = MAXIMUM_NUM_OF_REQUESTS_PER_BATCH
for i in range(0, len(batch), step):
  small_batch = batch[i:i+step]
  _ = client.batch_write_item(
    RequestItems = {
      'SessionStore': small_batch
    }
  )


end = time.perf_counter()
secs = end - start
secs = round(secs, 3)
print(f"{secs}s")