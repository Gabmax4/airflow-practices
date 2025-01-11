from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myfunction():
    pass

with DAG(
    dag_id="06-1-monitoring",
    description="Monitoreando nuestro DAG",
    schedule_interval="@daily",  # Corregido a "@daily"
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2024, 12, 31)  # Actualizado a una fecha futura
) as dag:

    t1 = BashOperator(
        task_id="tarea1",
        bash_command="sleep 2 && echo 'Primera tarea!'"
    )

    t2 = BashOperator(
        task_id="tarea2",
        bash_command="sleep 2 && echo 'Segunda tarea!'"
    )

    t3 = BashOperator(
        task_id="tarea3",
        bash_command="sleep 2 && echo 'Tercera tarea!'"
    )

    t1 >> t2 >> t3