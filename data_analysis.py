import  json
import pandas as pd

with open('cleaned_commit.json','r') as f:
    data=json.load(f)

df=pd.DataFrame(data)
print(df.head())
