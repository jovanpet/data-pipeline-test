import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import elt


args={
   'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag=DAG(
    dag_id="twitter_test_airflow",
    description="Testing fetching tweets and pipelining to AWS",
    default_args=args,
    schedule_interval=datetime.timedelta(days=1)
)

run = PythonOperator(task_id="example_python_operator", python_callable= elt.run_etl(), dag=dag)