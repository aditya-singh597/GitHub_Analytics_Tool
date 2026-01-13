import json

clean_commit=[]

with open('commits.json', 'r') as f:
    data=json.load(f)

for commits in data:
    clean_commit.append({"sha":commits.get("sha"),"author":commits.get("commit",{}).get("author",{}).get("name"),"date":commits.get("commit",{}).get("author",{}).get("date")})

with open('cleaned_commit.json','w') as f:
    json.dump(clean_commit,f,indent=4)
