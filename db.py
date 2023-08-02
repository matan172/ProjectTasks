import sqlite3
from oop import Task




def setup_tasks_tasks(filename="tasks.sqlite"):
    """
    setup database(if not exists)
    1.tasks
        ~ taskid      :int
        ~ date_added  :text
        ~ date_finish :text
        ~ desc        :text
        ~ completed   :bool

    """
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        statement1 = """
        CREATE TABLE IF NOT EXISTS tasks (taskid INTEGER PRIMARY KEY, date_added text , date_finish TEXT, desc text, completed bool)
    """     

        cur.execute(statement1)
        conn.commit()




def query_db(statement, filename="tasks.sqlite"):
        """
        get <- string(sql statement) 
        ! execute in <filename>.sqlite and commit !
        returns -> cursur.fetchall() from connection
        """
        with sqlite3.connect(filename) as conn:
            cur=conn.cursor()
            cur.execute(statement)
            conn.commit()
        return cur.fetchall()

def insert_tasks_sql(arr:list,filename="tasks.sqlite"):
    """
    get <- list of Task objects

    returns ->string(sql statement) to add
        them to customer table
    """
    statement = """
     INSERT INTO tasks
    (date_added, date_finish , desc , completed)
    VALUES 
    """
    lst = []
    for task in arr:
        lst.append( f"('{task.date_added}','{task.date_finish}','{task.desc}','{task.completed}')")
        
    statement += ",".join(lst)+';'
    return statement

def create_Task(date_added,date_finish,desc,completed=False):
    """
     add Task to  DB tasks TABLE tasks 
    """
    task = Task(date_added=date_added,date_finish=date_finish,desc=desc,completed=completed)
    query_db(insert_tasks_sql((task,)))
     
     


    

setup_tasks_tasks()

