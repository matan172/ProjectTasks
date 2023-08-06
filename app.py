import db
from flask import Flask,redirect,render_template,request
from datetime import datetime

app = Flask(__name__)
app.debug = True

today = datetime.today().strftime('%Y-%m-%d')
# -------- show --------
@app.route('/', methods=["POST","GET"])
def home():
    tasks = db.task_objects_bystate("False")
    if request.method == "POST":
        q = request.form["search"]
        tasks = db.filter_tasks(tasks,q)

    return render_template("todo.html", 
                           tasks=tasks,
                           today=datetime.today().strftime('%Y-%m-%d'),)


@app.route('/completed',methods=["POST","GET"])
def completed():
    tasks = db.task_objects_bystate("True")
    if request.method == "POST":
        q = request.form["search"]
        tasks = db.filter_tasks(tasks,q)
    return render_template("todo.html",
                        tasks= tasks,
                        today=datetime.today().strftime('%Y-%m-%d'),
                           )

@app.route('/all',methods=["POST","GET"])
def all():
    tasks = db.task_objects()
    if request.method == "POST":
        q = request.form["search"]
        tasks = db.filter_tasks(tasks,q)
    return render_template("todo.html",
                        tasks= tasks,
                        today=datetime.today().strftime('%Y-%m-%d'),
                           )
    
# -------- new task -------

@app.route('/addTask',methods=['GET', 'POST'])
def addTask():
    cdate = datetime.today().strftime('%Y-%m-%d')
    fdate = str(request.args["fdate"])
    desc = request.args["desc"]
    db.create_Task(date_added=cdate,date_finish=fdate,desc=desc)
    return redirect("/")

# -------task edit ------


@app.route('/completeTask', methods=["GET"])
def complete_task():
    taskid = request.args["taskid"]
    db.completeTask(taskid)
    return redirect('/')

@app.route('/renewTask', methods=["GET"])
def renew_task():
    taskid = request.args["taskid"]
    db.completeTask(taskid, False)
    return redirect('/completed')

@app.route("/updateTask", methods = ["POST","GET"])
def updatetask():
    if request.method == "GET":
        print(1)
        taskid = request.args["taskid"]
        id,task = db.get_task_info(taskid)
        return render_template('update.html', taskid = id, task = task , today=datetime.today().strftime('%Y-%m-%d') )
        
    else:
        date = request.form["date"]
        id = request.form["taskid"]
        desc = request.form['desc']
        
        db.update_fdate(taskid=id,date=date)
        db.update_desc(taskid=id,desc=desc)
        return redirect("/")
    


    



