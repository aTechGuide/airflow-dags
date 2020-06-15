from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 10),
    'email': ['kamranalinitb@gmail.com']
}

dag = DAG(
    'basic6h',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval="0 */6 * * *",
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t1