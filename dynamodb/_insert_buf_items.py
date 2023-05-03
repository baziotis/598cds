import boto3
import pandas as pd

dynamodb = boto3.resource('dynamodb')
table_name = 'BufTable'
table = dynamodb.Table(table_name)

df = pd.read_csv('items_buf.csv')

dicts = [row.to_dict() for _, row in df.iterrows()]

for d in dicts:
  table.put_item(Item=d)
# END OF LOOP #