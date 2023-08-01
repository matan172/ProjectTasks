

class Task():
    def __init__(self,date_added,date_finish,desc,completed=False) -> None:
        self.date_added = date_added
        self.date_finish = date_finish
        self.desc = desc
        self.completed = completed

    def complete(self):
        self.completed=True
    