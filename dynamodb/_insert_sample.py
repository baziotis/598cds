import boto3
import datetime
import uuid
import pandas as pd
import time

# Insert the first 1000 rows. This is used when we want less data
# so that e.g., we don't pay for extra writes and reads.

dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

df = pd.read_csv('items.csv')
df = df[:1000]

dicts = [row.to_dict() for _, row in df.iterrows()]

for d in dicts:
  table.put_item(Item=d)
# END OF LOOP #