from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'yvvon',
    'depends_on_past': False,
    'retries': 1,

}

with DAG(
    'dbt_airflow_pipeline',
    default_args=default_args,
    description='A simple Airflow dbt pipeline',
    schedule_interval='@daily',  # Define how often the DAG should run
    start_date=datetime(2024, 9, 29),
    catchup=False,  # Don't run past DAG runs when starting Airflow
) as dag:
    dbt_debug = BashOperator(
        task_id='dbt_debug',
        bash_command='dbt debug --profiles-dir /home/gitpod/.dbt'
    )

# this will run dbt models
    dbt_run = BashOperator(
        task_id = 'dbt_run',
        bash_command='dbt run --profiles-dir /home/gitpod/.dbt'

    )
# Define the task pipeline
dbt_debug >> dbt_run