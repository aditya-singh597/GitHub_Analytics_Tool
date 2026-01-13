import sys
print(sys.path)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR


import matplotlib
matplotlib.use("Agg")  # force safe backend
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib
print("Matplotlib loaded from:", matplotlib.__file__)

#daily_commits = pd.read_csv("daily_commit_frequency.csv")
daily_commits = pd.read_csv(DATA_DIR / "daily_commit_frequency.csv")
daily_commits["date"] = pd.to_datetime(daily_commits["date"])

plt.figure()
plt.plot(daily_commits["date"], daily_commits["commit_count"])
plt.xlabel("Date")
plt.ylabel("Number of Commits")
plt.title("Daily Commit Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_commit_frequency.png")
plt.close()


total_days = len(daily_commits)
active_days = len(daily_commits[daily_commits["commit_count"] > 0])
inactive_days = total_days - active_days

plt.figure()
plt.bar(["Active Days", "Inactive Days"], [active_days, inactive_days])
plt.title("Commit Consistency Overview")
plt.ylabel("Number of Days")
plt.savefig("commit_consistency.png")
plt.close()

