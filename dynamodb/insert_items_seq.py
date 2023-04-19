import boto3
import datetime
import uuid
import pandas as pd
import time

dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

df = pd.read_csv('items.csv')
# Randomize
df = df.sample(frac=1, random_state=10)

dicts = [row.to_dict() for _, row in df.iterrows()]

start = time.perf_counter()
for d in dicts:
  table.put_item(Item=d)
# END OF LOOP #

end = time.perf_counter()
secs = end - start
secs = round(secs, 3)
print(f"{secs}s")