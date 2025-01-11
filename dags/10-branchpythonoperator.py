from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date

defaul_args = {
'start_date': datetime (2024,12,30),
'end_date': datetime (2024,12,31)
}

def _choose(**context):

    if context["logical_date"].date() < date(2025,1,5):
        return "Finish_30_dic"
    return "Finish_31_dic"

with DAG ('10-branching',
          schedule_interval = '@daily',
          default_args = defaul_args) as dag:
    branching = BranchPythonOperator(
        task_id = "branch",
        python_callable= _choose
    )

    finish_30 = BashOperator(
        task_id = 'Finish_30_dic',
        bash_command = "echo 'Runing {{ds}}'"
    )
    finish_31 = BashOperator(
        task_id='Finish_31_dic',
        bash_command="echo 'Runing {{ds}}'"
    )

    branching >> [finish_30, finish_31]