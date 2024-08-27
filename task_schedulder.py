class Job:
    def __init__(self, task, execute_at) -> None:
        self.task = task
        self.execute_at = execute_at
        self.next = None
    

class Scheduler:
    def __init__(self) -> None:
        self.start = None

    def add_task(self, task, execute_at) -> None:
        pass