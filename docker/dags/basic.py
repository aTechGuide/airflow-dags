from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 14, 0, 0, 0),
    'catchup_by_default': False,
    'email': ['kamranalinitb@gmail.com']
}

dag = DAG(
    'basic_4',
    default_args=default_args,
    description='A simple tutorial DAG',
    catchup=False,
    schedule_interval="10 10 * * *",
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t1