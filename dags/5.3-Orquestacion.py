from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="5.3-Orquestacion",
    description="Probando la orquestacion",
    schedule_interval="@monthly",
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2024, 12, 31)
) as dag:
    t1 = EmptyOperator(task_id = "tarea1")
    t2 = EmptyOperator(task_id="tarea2")
    t3 = EmptyOperator(task_id="tarea3")
    t4 = EmptyOperator(task_id="tarea4")
    t1 >> t2 >> t3 >> t4