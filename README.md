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

Auto generating the table in PostgreSQL: `python -m scripts.init_db`

Loading the data to PostgreSQL: `python -m scripts.load_spotify_data`

Starting Docker:

`docker compose up airflow-init`

`docker compose up`

Go to `http://localhost:8080` in your browser and login with username and password 'airflow'