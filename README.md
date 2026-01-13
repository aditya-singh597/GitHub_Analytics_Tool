GitHub Analytics Tool

A Python-based tool that analyzes GitHub repository commit activity using the GitHub REST API. It processes raw API data into structured datasets and generates visual insights while avoiding repeated API calls.

Overview:

The project follows a complete analytics pipeline:
API → JSON → Cleaned Data → CSV → Analysis → Visualization
It focuses on modular design, reproducibility, and real-world data engineering practices.

Features:

GitHub REST API integration with pagination
Secure authentication via environment variables
JSON data cleaning and normalization
CSV caching to prevent repeated API calls
Commit frequency and consistency analysis
Headless-safe visualizations saved as image files

Project Structure:

GitHub_Analytics_Tool/
├── api_calling.py
├── clearing_data.py
├── data_analysis.py
├── visualization/
│   ├── __init__.py
│   └── visualization.py
├── commits_clean.csv
├── daily_commit_frequency.csv
├── daily_commit_frequency.png
├── commit_consistency.png
└── README.md

Technologies:

Python, GitHub REST API, Requests, Pandas, Matplotlib
Running the Project
Install dependencies
pip install requests pandas matplotlib

Run the pipeline:

python api_calling.py
python clearing_data.py
python data_analysis.py
python -m visualization.visualization

Challenges Addressed:

Python import resolution and module-based execution
Virtual environment and interpreter mismatches
Python 3.14 compatibility issues with matplotlib
Non-interactive plotting backends
File path and working directory handling

Author:
Aditya Singh
