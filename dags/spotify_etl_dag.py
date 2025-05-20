# dags/spotify_etl_dag.py

# import needed airflow classes and modules
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import logging

# ---- EXTRACT ----
def extract_data():
    logging.info("Extract step: Data already exists in PostgreSQL. Skipping download")

# ---- TRANSFORM ----
def transform_data():
    # initialize postgreshook to connect to the postgres database
    hook = PostgresHook(postgres_conn_id='spotify_postgres') # connection id in airflow connection

    # get database connection
    with hook.get_conn() as conn:
        with conn.cursor() as cursor:
            # execute SQL to create a summary table of artists and their song counts
            cursor.execute("DROP TABLE IF EXISTS artist_summary;")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS artist_summary AS
                SELECT artist, COUNT(*) AS song_count
                FROM spotify_songs
                GROUP BY artist;
            """)
            logging.info("Transform step: Created artist_summary table")

# ---- LOAD ----
def load_data():
    logging.info("Load step: Data is already loaded. You can add export/upload logic here")

# ---- DAG CONFIGURATION ----
# default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
with DAG(
    dag_id = 'spotify_etl_pipeline', # unique ID for DAG
    default_args = default_args, # default arguments
    schedule_interval = '@daily', # DAG runs once a day
    start_date = datetime(2025, 5, 20), # DAG starts from this date
    catchup = False, # prevent backfilling of previous dates
    description = 'ETL pipeline for Spotify data in PostgreSQL', # description
    tags = ['etl', 'spotify'], # tags for filtering in the airflow UI
) as dag:
    
    dag.doc_md = """
    ### Spotify ETL Pipeline

    This DAG performs a basic ETL process:
    - **Extract:** Data already loaded into PostgreSQL, no action needed.
    - **Transform:** Summarizes artist song counts into a new table.
    - **Load:** Placeholder for future export steps (e.g., S3, BigQuery).
    """
    
    # extract data
    extract = PythonOperator(
        task_id = 'extract', # unique task id
        python_callable = extract_data, # function to run
    )

    # transform data
    transform = PythonOperator(
        task_id = 'transform', # unique task id
        python_callable = transform_data, # function to run
    )

    # load data
    load = PythonOperator(
        task_id = 'load', # unique task id
        python_callable = load_data, # function to run
    )
    
    # define task dependencies
    extract >> transform >> load