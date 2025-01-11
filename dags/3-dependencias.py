from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    print('Hello bandita de Platzi')

def print_task3():
    print('Esta es la tarea 3')

with DAG(
    dag_id='Dependencias',  # Corrección aquí
    description='Creando Dependencias entre tareas',
    schedule_interval='@once',
    start_date=datetime(2023, 9, 1)
) as dag:
    t1 = PythonOperator(
        task_id='tarea1',
        python_callable=print_hello
    )

    t2 = BashOperator(
        task_id='tarea2',
        bash_command="echo 'tarea2'"
    )

    t3 = PythonOperator(
        task_id='tarea3',
        python_callable=print_task3
    )

    t4 = BashOperator(
        task_id='tarea4',
        bash_command="echo 'tarea4'"
    )

    t1 >> t2 >> [t3, t4]
