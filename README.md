# Data Pipeline Project: Spotify Streaming Analysis

## 🎯 Project Goals
- Build a robust data pipeline to ingest, clean, and analyze Spotify's most streamed songs in 2024.
- Demonstrate orchestration with Apache Airflow.
- Store and query data using PostgreSQL.
- Perform exploratory data analysis and visualize trends in music streaming.

## 🔧 Tools & Technologies
- Python 3.11+
- Apache Airflow
- PostgreSQL
- Pandas, NumPy, Matplotlib
- Jupyter Notebooks
- Docker
- Git / GitHub

## ⚙️ Setting Up the Environment

### 🐍 Python Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 📦 Install Dependencies
```bash
pip install --upgrade pip
pip install pandas jupyter notebook
```

## 📁 Running the ETL Scripts Manually

### Extract and Transform
```
python scripts/extract_spotify_data.py
python scripts/transform_spotify_data.py
```

### Initialize and Load Data into PostgreSQL
```
python -m scripts.init_db
python -m scripts.load_spotify_data
```

## 🚀 Running the Airflow DAG

### 🐳 Starting Airflow with Docker

Start the Airflow services:

Start the `spotify-data-pipeline` engine in Docker Desktop

Connect to Docker:

```
docker compose up airflow-init
docker compose up
```

Navigate to the Airflow UI: http://localhost:8080

Login:
```
Username: airflow
Password: airflow
```

### 📂 DAG Overview

The DAG is defined in:

`dags/spotify_etl_dag.py`

It includes the following tasks:

`extract`: Logs that data is preloaded (no API call made).

`transform`: Creates a summary table artist_summary in PostgreSQL.

`load`: Placeholder for future export/upload logic.

Schedule: The DAG runs daily (`@daily`).

### ▶️ Running the DAG

1. In the Airflow UI, locate the DAG named `spotify_etl_pipeline`.

2. Toggle the switch to Enable it.

3. Click the Play button to Trigger DAG manually.

## ✅ Testing the ETL Pipeline End-to-End

To verify the pipeline:

1. Clean slate (optional):
Drop existing summary table in PostgreSQL:

`DROP TABLE IF EXISTS artist_summary;`

2. Trigger the DAG via Airflow.

3. Verify success: Check that the new summary table was created:

`SELECT * FROM artist_summary LIMIT 10;`

You should see a list of artists with corresponding song counts.

## 🔍 Airflow Connection Setup

In the Airflow UI → Admin > Connections, create a connection:

- Conn Id: `spotify_postgres`

- Conn Type: `Postgres`

- Host: `host.docker.internal` (or `localhost` depending on your OS)

- Schema: `your_database_name`

- Login: `your_postgres_username`

- Password: `your_postgres_password`

- Port: `4000` (or your actual PostgreSQL port)

## 🛠️ Troubleshooting
- Transform step fails:

  - Make sure the database name in the connection matches the actual PostgreSQL database.

  - Confirm the port and host configuration are correct for Docker.

- Connection error (`OperationalError`):

  - PostgreSQL might not be accessible from inside the Docker container.

  - Use `host.docker.internal` for macOS/Windows or `172.17.0.1` on Linux.

## 📌 Future Improvements

- Add alerting/email notification on DAG failure.

- Export final results to a data warehouse (e.g., BigQuery).

- Add more complex transformations or visualizations.