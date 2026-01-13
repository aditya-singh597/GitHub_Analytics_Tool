import requests
import os

Token=os.getenv("GITHUB_TOKEN")
repo="GitHub_Analytics_Tool"
user="aditya-singh597"

url=f"https://api.github.com/repos/{user}/{repo}/commits"

headers={"Authorization": f"Bearer {Token}", "Accept": "application/vnd.github+json"}
all_commits=[]
page=1

while True:
    params={"per_page":100,"page":page}
    response=requests.get(url,headers=headers,params=params)
    data=response.json()
    print(data)

    if not data:
        break

    all_commits.extend(data)
    page+=1


print(f"Fetched {len(all_commits)} commits")