# A small utility to recover the deleted user

import boto3
import pandas as pd

dynamodb = boto3.resource('dynamodb')
table_name = 'SessionStore'
table = dynamodb.Table(table_name)

df = pd.read_csv('items.csv')
adjutant = df['Username'] == 'adjutant'
df = df[adjutant]

dicts = [row.to_dict() for _, row in df.iterrows()]

for d in dicts:
  table.put_item(Item=d)