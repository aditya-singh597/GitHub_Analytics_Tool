import  json
import pandas as pd

with open('cleaned_commit.json','r') as f:
    data=json.load(f)

df=pd.DataFrame(data)
print(df.head())

df['date']=pd.to_datetime(df['date'])
daily_commits = (
    df
    .set_index('date')
    .resample('D')
    .size()
    .reset_index(name='commit_count')
)

author_commit_count = (
    df
    .groupby("author")
    .size()
    .reset_index(name="total_commits")
)

active_days=daily_commits[daily_commits['commit_count']>0]
consistency = len(active_days) / len(daily_commits)
print(f"Consistency: {consistency:.2%}")

df.to_csv("commits_clean.csv", index=False)
author_commit_count.to_csv("author_commit_count.csv", index=False)
