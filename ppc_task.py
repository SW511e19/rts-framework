import task
import time


class PPC_Task(task.Task):

    def task_body(self):
        print("Start PPC")
        time.sleep(3)
        print("Done with PPC")
        self.end_task()
        return

    def __init__(self, startTime, deadline=1000, priority=1337):
        super().__init__(startTime, deadline, priority)
