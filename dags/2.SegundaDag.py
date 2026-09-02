import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(

    dag_id = "segunda_dag",
    description = "Minha segunda dag",
    schedule = None,
    start_date = pendulum.datetime(2025,1,1,tz="America/Sao_Paulo"),
    catchup = False,
    tags = ["curso","exemplo"]
) as dag:

    task1 = BashOperator(task_id='tsk1',bash_command="sleep 5")
    task2 = BashOperator(task_id='tsk2',bash_command="sleep 5")
    task3 = BashOperator(task_id='tsk3',bash_command="sleep 5")

    #Fan-out
    #Quando uma DAG/tarefa dispara ou se ramifica para duas ou mais tarefas em paralelo.

    task1 >> [task2 , task3]