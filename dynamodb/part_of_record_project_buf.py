import boto3
import time
import pandas as pd

dynamodb = boto3.resource('dynamodb')
table_name = 'BufTable'
table = dynamodb.Table(table_name)

df = pd.read_csv('items_buf.csv')
# Keep the first 1000 because this is the sample we've inserted
df = df[:1000]
# Randomize
df = df.sample(frac=1, random_state=10)

# Add to all rows some number

dicts = [row.to_dict() for _, row in df.iterrows()]

start = time.perf_counter()
for row in dicts:
  username = row["username"]
  # Say we get only `Username` and `CreatedAt`
  resp = table.get_item(
      Key={
        'username': username
      },
      ProjectionExpression='username, col'
  )
  item = resp["Item"]
# END OF LOOP #

end = time.perf_counter()
secs = end - start
secs = round(secs, 3)
print(f"{secs}s")