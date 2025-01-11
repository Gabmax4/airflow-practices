from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

templated_Command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}

"""
with DAG(dag_id = "8-Templating",
         description = "Exaple using Templates",
         schedule_interval = "@daily",
         start_date = datetime (2024,12,28),
         end_date= datetime (2024,12,30),
         max_active_runs=1) as dag:
    t1 = BashOperator (task_id = "Tarea1",
                       bash_command= templated_Command,
                       params={"filenames": ["file1.txt", "file2.txt"]},
                       depends_on_past = True)