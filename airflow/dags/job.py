from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Default arguments
default_args = {
    'owner': "airflow",
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

# Define the DAG
dag = DAG(
    'multi_job_hello_world',
    default_args=default_args,
    description="A multi-job Hello World DAG",
    schedule_interval='*/30 0 * * *',  # Runs every 30 minutes during midnight hour
    catchup=False,
)

# Task 1: Start
def start():
    print("Starting the workflow...")

start_task = PythonOperator(
    task_id='start_task',
    python_callable=start,
    dag=dag
)

# Task 2: Process
def process():
    print("Processing the task...")

process_task = PythonOperator(
    task_id='process_task',
    python_callable=process,
    dag=dag
)

# Task 3: End
def end():
    print("Workflow complete.")

end_task = PythonOperator(
    task_id='end_task',
    python_callable=end,
    dag=dag
)

# Set task dependencies
start_task >> process_task >> end_task
