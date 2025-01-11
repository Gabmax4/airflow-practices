from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

def print_hello():
    print('Hello bandita de Platzi')

with DAG(
    dag_id='customoperator',  # Corrección aquí
    description='Nuestro primer Custom operator',
    schedule_interval='@once',
    start_date=datetime(2023, 9, 1)
) as dag:
    t1 = HelloOperator(
        task_id='Hello',
        name='Freddy'
    )