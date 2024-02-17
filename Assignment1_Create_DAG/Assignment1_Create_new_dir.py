import os
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": days_ago(1),
    "retry_delay": timedelta(minutes=1),
}

def create_new_dir():
    dag_folder = os.path.dirname(__file__)
    new_dir = os.path.join(dag_folder, 'test_dir')

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Directory '{new_dir}' created successfully.")
    else:
        print(f"Directory '{new_dir}' already exists.")

with DAG(
    dag_id='Assignment1_Create_DAG',
    description='Assignment1_Create_DAG',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    tags=['Python', 'Assignment1', 'operators']
) as dag:
    create_new_dir_task = PythonOperator(
        task_id='Assignment1_Create_NEW_DIR',
        python_callable=create_new_dir
    )
