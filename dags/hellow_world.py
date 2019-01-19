import datetime
from airflow import models
from airflow.operators.bash_operator import BashOperator

DAG_NAME = 'hellow_world'

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(days=1) + datetime.timedelta(hours=9),
    datetime.datetime.min.time()
)

default_dag_args = {
    'owner': 'HagaSpa',
    'start_date': yesterday,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': models.Variable.get('project_id')
}

with models.DAG(
    dag_id=DAG_NAME,
    schedule_interval="@once",
    default_args=default_dag_args) as dag:
    
        t1 = BashOperator(
            task_id='task1',
            bash_command='echo Hellow World'
        )
