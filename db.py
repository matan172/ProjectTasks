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
     
     
def show_tasks():
     statement = "SELECT * FROM tasks"
     return query_db(statement)

def task_objects():
    """
    <- [(id, taskOBJ)**,]
    """
    ret_list = []
    for task in show_tasks():
        ret_list.append((task[0],
             Task(date_added=task[1],
             date_finish=task[2],
             desc=task[3],
             completed=task[4])))
    return ret_list

def task_objects_bystate(state):
    """
    <"False"> = not completed | <True> = completed 
    <-  [(id, taskOBJ)**,]
    """
    ret_list = []
    for task in show_tasks():
        if task[4] == state:
            ret_list.append((task[0],
                Task(date_added=task[1],
                date_finish=task[2],
                desc=task[3],
                completed=task[4])))
    return ret_list

def filter_tasks(db,q):
    ret_list = []
    for task in db:
        for i in task[1].__dict__.values():
            if q.lower() in str(i):
                ret_list.append(task)
                break
    return ret_list



def completeTask(taskid, complete = True):
    if complete:
        statement= f"UPDATE tasks SET completed = 'True' WHERE taskid = '{taskid}';"
        query_db(statement)

    else:
        statement= f"UPDATE tasks SET completed = 'False' WHERE taskid = '{taskid}';"
        query_db(statement)

def get_task_info(taskid):
    statement = f"SELECT * FROM tasks WHERE taskid = '{taskid}';"
    task = query_db(statement)[0]
    return (task[0],
                Task(date_added=task[1],
                date_finish=task[2],
                desc=task[3],
                completed=task[4]))


def update_desc(taskid,desc):
    statement = f"UPDATE tasks SET desc = '{desc}' WHERE taskid = '{taskid}';"
    query_db(statement=statement)
    

def update_fdate(taskid,date):
    statement = f"UPDATE tasks SET date_finish = '{date}' WHERE taskid = '{taskid}';"
    query_db(statement=statement)



setup_tasks_tasks()
    
print(get_task_info(1))
