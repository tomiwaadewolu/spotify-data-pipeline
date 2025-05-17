# Data Pipeline Project: Spotify Streaming Analysis

## 🎯 Project Goals
- Build a robust data pipeline to ingest, clean, and analyze Spotify's most streamed songs in 2024.
- Demonstrate orchestration with Apache Airflow.
- Store and query data using PostgreSQL or Google Cloud Platform (BigQuery).
- Perform exploratory data analysis and visualize trends in music streaming.

## 🔧 Tools & Technologies
- Python 3.11+
- Apache Airflow
- PostgreSQL / Google Cloud (BigQuery)
- Pandas, NumPy, Matplotlib / Seaborn
- Jupyter Notebooks
- Docker (optional for containerized Airflow)
- Git / GitHub

## Setting Up Python Environment
`python -m venv venv`

`venv\Scripts\activate` (specific to Windows)

`pip install --upgrade pip`

Initial dependencies: `pip install pandas jupyter notebook`

Running the python scripts: 

`python scripts/extract_spotify_data.py`

`python scripts/transform_spotify_data.py`