from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5,23)
}

dag = DAG(
    dag_id = 'DAG_1',
    default_args = default_args,
    schedule_interval = '@once',
    catchup = False
)

task1 = DummyOperator(task_id = 'task1', dag = dag)
task2 = DummyOperator(task_id = 'tast2', dag = dag)

task1 >> task2