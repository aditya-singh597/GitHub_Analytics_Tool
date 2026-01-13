📊 GitHub Analytics Tool

A Python-based analytics tool that extracts commit data from the GitHub REST API, processes it into structured datasets, and generates visual insights such as commit frequency and consistency — all while avoiding repeated API calls.

🚀 Project Overview

The GitHub Analytics Tool is designed to analyze repository activity in a clean, scalable, and reproducible way.
It follows a complete data pipeline:

API → JSON → Cleaned Data → CSV → Analysis → Visualization

This project focuses not just on what data is analyzed, but also how it is engineered and visualized in a production-safe manner.

✨ Key Features

🔐 Secure GitHub API access using environment variables

📡 Handles API pagination to fetch complete commit history

🧹 Cleans and extracts only relevant fields from raw JSON

💾 Saves processed data to CSV to avoid repeated API calls

📈 Computes commit frequency and consistency metrics

📊 Generates visualizations as image files (headless-safe)

🧱 Modular project structure (analysis, cleaning, visualization separated)

🗂️ Project Structure
GitHub_Analytics_Tool/
│
├── api_calling.py              # Fetches commit data from GitHub API
├── clearing_data.py            # Cleans raw JSON into structured format
├── data_analysis.py            # Computes frequency & consistency metrics
│
├── visualization/
│   ├── __init__.py
│   └── visualization.py        # Generates plots
│
├── cleaned_commit.json         # Cleaned commit data (JSON)
├── commits_clean.csv           # Commit-level dataset
├── daily_commit_frequency.csv  # Daily aggregated commit counts
│
├── commit_consistency.png      # Visualization output
├── daily_commit_frequency.png  # Visualization output
│
├── README.md
└── .gitignore

🔧 Technologies Used

Python

GitHub REST API

Requests – API calls

Pandas – data processing & analysis

Matplotlib – visualization

Pathlib – robust file handling

🔐 Authentication

GitHub authentication is handled using a Personal Access Token (PAT) stored as an environment variable:

GITHUB_TOKEN=your_token_here


This ensures:

No hardcoded secrets

Secure API access

Cleaner version control

📊 Analytics Performed
1️⃣ Commit Frequency

Number of commits per day

Aggregated using time-based resampling

2️⃣ Commit Consistency

Ratio of active days to total days

Helps measure regularity of contributions

3️⃣ Author Contribution Summary

Total commits per author

Scalable to multi-contributor repositories

📈 Visualizations
📅 Daily Commit Frequency

Shows how commits are distributed across days.

📊 Commit Consistency Overview

Compares active vs inactive days.

Visualizations are saved as .png files instead of being displayed interactively, making the tool compatible with headless environments (CI/CD, servers).

⚙️ How to Run the Project
1️⃣ Create & activate virtual environment
python -m venv .venv

2️⃣ Install dependencies
pip install requests pandas matplotlib

3️⃣ Fetch commit data
python api_calling.py

4️⃣ Clean raw data
python clearing_data.py

5️⃣ Analyze commits
python data_analysis.py

6️⃣ Generate visualizations (module-based)
python -m visualization.visualization

🧠 Challenges Faced & Learnings

Python import resolution conflicts

Module vs script execution differences

Python 3.14 compatibility issues with scientific libraries

Handling non-interactive plotting backends

Importance of absolute file paths

These challenges helped reinforce real-world Python engineering practices, not just syntax.

🌱 Future Improvements

Commit streak analysis

Weekly & monthly aggregation

GitHub-style contribution heatmap

CLI interface for user input

Multi-repository analytics

Automated report generation

🏁 Conclusion

This project demonstrates a complete analytics workflow, from data ingestion to visualization, while following best practices in:

code organization

security

reproducibility

debugging

It is designed to scale as repository data grows and can serve as a strong foundation for more advanced developer analytics tools.

👤 Author

Aditya Singh
Engineering student | Python | Data Analytics | Systems Thinking
