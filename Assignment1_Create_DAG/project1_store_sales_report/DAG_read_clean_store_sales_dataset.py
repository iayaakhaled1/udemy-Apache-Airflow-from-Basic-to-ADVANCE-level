from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

import pandas as pd 
import os

import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'admin',
    'depends_on_past': False,    
    'start_date': days_ago(1)
}

def check_path():
    dag_folder = os.path.dirname(__file__)
    file_path = os.path.join(dag_folder, 'raw_store_transactions.csv')
    output_path = os.path.join(dag_folder, 'output_files')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
        print(f"Directory '{output_path}' created successfully.")
    else:
        print(f"Directory '{output_path}' already exists.")
    return file_path, output_path

def clean_dataframe():
    file_path, output_path = check_path()
    df = pd.read_csv(file_path)
    df['STORE_LOCATION'] = df['STORE_LOCATION'].replace(r'[^\w\s]|_', '', regex=True)
    df['MRP'] = df['MRP'].replace(r'[^\w\s]|_', '', regex=True)
    df['CP'] = df['CP'].replace(r'[^\w\s]|_', '', regex=True)
    df['DISCOUNT'] = df['DISCOUNT'].replace(r'[^\w\s]|_', '', regex=True)
    df['SP'] = df['SP'].replace(r'[^\w\s]|_', '', regex=True)
    df['Date'] = pd.to_datetime(df['Date'])
    file_output_path = os.path.join(output_path, 'clean_raw_store_transactions.csv')
    df.to_csv(file_output_path, index=False)
    return file_output_path

# def execute_flow():
#     file_path, output_path = check_path()
#     cleaned_file_path = clean_dataframe(file_path, output_path)


with DAG(
    dag_id='Store-Sales-data-flow',
    description='Store sales data pipeline using airflow',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None
) as dag:

    check_if_file_exist = PythonOperator(
        task_id='check_path',
        python_callable=check_path
    )

    clean_store_sales_dataframe = PythonOperator(
        task_id='clean_store_sales_dataframe',
        python_callable=clean_dataframe
    )

    # execute_flow_to_read_clean_file = PythonOperator(
    #     task_id='read_clean_file_execute_flow',
    #     python_callable=execute_flow
    # )

    check_if_file_exist >> clean_store_sales_dataframe 
