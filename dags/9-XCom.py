from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator

default_args = {'depends_on_past': True}

def myfunction (**context):
    print(int(context["ti"].xcom_pull(task_ids = 'Tarea2')) - 24)

with DAG(
    dag_id = "9-XCom",
    description = "Probando los XCOM",
    schedule_interval = "@once",
    start_date=datetime(2024,12,30),
    default_args = default_args,
    max_active_runs=1) as dag:

    t1 = BashOperator(
        task_id="Tarea1",
        bash_command="sleep 5 && echo $((3 * 8))"
    )

    t2 = BashOperator(
        task_id = "Tarea2",
        bash_command="sleep 3 && echo  {{ ti.xcom_pull(task_ids='Tarea1') }}"
    )

    t3 = PythonOperator(
        task_id = "Tarea3",
        python_callable = myfunction
    )

    t1 >> t2 >> t3
