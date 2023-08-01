from faker import Faker
from oop import Task

fake = Faker()



def Fake_tasks(n:int=10):
    """
    <- n
    -> [fake_Task*n]
    """
    ret_list = []
    for i in range(n):
        temp_task = Task(
            date_added=fake.date
