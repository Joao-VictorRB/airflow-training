import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(

    dag_id = "terceira_dag",
    description = "Minha terceira dag",
    schedule = None,
    start_date = pendulum.datetime(2025,1,1,tz="America/Sao_Paulo"),
    catchup = False,
    tags = ["curso","exemplo"]
) as dag:

    task1 = BashOperator(task_id='tsk1',bash_command="sleep 5")
    task2 = BashOperator(task_id='tsk2',bash_command="sleep 5")
    task3 = BashOperator(task_id='tsk3',bash_command="sleep 5")

    #Fan-in
    #Quando duas ou mais tarefas convergem para uma única tarefa.

    [task1 , task2] >> task3