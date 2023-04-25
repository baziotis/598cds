import boto3
import datetime
import uuid
import pandas as pd
import time
from pprint import pprint

client = boto3.client('dynamodb')
table_name = 'SessionStore'

df = pd.read_csv('items.csv')
# Randomize
df = df.sample(frac=1, random_state=10)

batch = []
for idx, row in df.iterrows():
  item = row.to_dict()
  low_level_item = {}
  for key, val in item.items():
    if key == 'SomeNumber':
      low_level_item[key] = {'N': val}
    else:
      low_level_item[key] = {'S': val}
  # END OF LOOP #
  req = {
    'PutRequest': {
      'Item': low_level_item
    }
  }
  batch.append(req)
# END OF LOOP #

# This is a constraint imposed by DynamoDB
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
