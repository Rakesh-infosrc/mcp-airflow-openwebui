from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define the tasks
def task1_function():
    print("Executing Task 1")
    return "Task 1 completed"

def task2_function():
    print("Executing Task 2")
    return "Task 2 completed"

def task3_function():
    print("Executing Task 3")
    return "Task 3 completed"

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
with DAG(
    'simple_example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Define the tasks
    task1 = PythonOperator(
        task_id='task1',
        python_callable=task1_function,
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=task2_function,
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=task3_function,
    )

    # Set task dependencies
    task1 >> task2 >> task3 