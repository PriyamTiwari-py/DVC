import pandas as pd
import os

# dic={
#     "name": ["Alice", "Bob", "Charlie"],
#     "age": [25, 30, 35],
#     "city": ["New York", "Los Angeles", "Chicago"]
# }

# df=pd.DataFrame(dic)

# os.makedirs("data", exist_ok=True)
# df.to_csv("data/people.csv", index=False)
# print("DataFrame saved to data/people.csv")

df=pd.read_csv("data/people.csv")
df.loc[df.shape[0]]=["David",40,"San Francisco"]

df.to_csv("data/people.csv", index=False)
print("DataFrame saved to data/people.csv")