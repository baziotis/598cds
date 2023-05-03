import pandas as pd
import random
import string

num_rows = 200
num_cols = 1000

random.seed(10)

# Create a list of random strings for each column
str_len = 200
random_strings = []
for i in range(num_cols):
  random_strings.append([''.join(random.choices(string.ascii_lowercase, k=str_len)) for j in range(num_rows)])

# Let's pretend we have a couple of users
usernames = ['bob', 'george', 'maria', 'stef']
row_user = [random.choice(usernames) for _ in range(num_rows)]

# Create a Pandas DataFrame from the random strings
d = {}
d['username'] = row_user
d = d | {'col'+str(i+1): random_strings[i] for i in range(num_cols)}
df = pd.DataFrame(d)
print(df)

avg_row_size = df.memory_usage(deep=True).sum() / len(df)
in_mb = avg_row_size / (1024**2)
print(in_mb)
df.to_csv('items_buf.csv', index=False)