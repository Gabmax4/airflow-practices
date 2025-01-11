from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print('Hello bandita de Platzi')

with DAG(
    dag_id='pythonoperator',  # Corrección aquí
    description='Nuestro primer Dag utilizando Python Operator',
    schedule_interval = '@once',
    start_date=datetime(2023, 9, 1)
) as dag:
    t1 = PythonOperator(
        task_id='Hello_with_python',
        python_callable=print_hello
    )