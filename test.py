from faker import Faker
from oop import Task
import db

fake = Faker()



def Fake_tasks(n:int=10):
    """
    <- n
    add fake tasks to DB tasks TABLE tasks
    -> none
    """
    for i in range(n):
        db.create_Task(date_added=fake.date(),
            date_finish=fake.date(),
            desc= fake.name())



# Fake_tasks() # to add 10 fake tasks