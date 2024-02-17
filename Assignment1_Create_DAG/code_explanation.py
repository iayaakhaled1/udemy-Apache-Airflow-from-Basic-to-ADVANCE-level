## old code ( with error ) 

from airflow import DAG
from datetime import datetime, timedelta
import pandas as pd
import os
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
#-------------------------------------------------------------------------------------#
default_args = {
"owner": "admin",
"depends_on_past": False,
"start_date": days_ago(1),
# "email": ["airflow@airflow.com"],
# "email_on_failure": False,
# "email_on_retry": False,
# "retries": 1,
"retry_delay": timedelta(minutes=1),
# 'queue': 'bash_queue',
# 'pool': 'backfill',
# 'priority_weight': 10,
# 'end_date': datetime(2016, 1, 1),
}

def create_new_dir():
base_dir = r'folder_path'
new_dir = os.path.join(base_dir, 'test_dir')

Copy
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created successfully.")
else:
    print(f"Directory '{new_dir}' already exists.")
with DAG(
dag_id = 'Assignment1_Create_DAG',
description = 'Assignment1_Create_DAG',
default_args = default_args,
start_date = days_ago(1),
schedule_interval = None,
tags = ['Python', 'Assignment1', 'operators']
) as dag:
create_new_dir_task = PythonOperator(
task_id = 'Assignment1_Create_NEW_DIR',
python_callable = create_new_dir
)

#----------------------------------------------------------------------------------------------------------#
- The error when running the code in Airflow is likely due to the fact that the directory path doesn't exist in the Airflow environment.
- When Airflow executes tasks, it does so within its own working directory. Therefore, you need to provide a relative path or an absolute path that is relative to the Airflow working directory.
- You can use the dag_folder variable to determine the current working directory of your DAG file and create the directory relative to that.

#----------------------------------------------------------------------------------------------------------#
Here's an updated version of the code that uses the dag_folder variable to create the directory within the Airflow working directory:

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
In this updated code, the dag_folder variable is used to determine the directory of the current DAG file. The new_dir path is then created by joining dag_folder with the directory name 'test_dir'. This ensures that the directory is created relative to the Airflow working directory.

Please note that the __file__ variable is used to refer to the current file path. Make sure to adjust the directory structure within the DAG folder accordingly to match your desired directory structure.
