import task
import time


class PCP_Task(task.Task):

    def task_body(self):
        print("Start PCP")
        time.sleep(3)
        print("Done with PCP")
        self.task_completed = True
        return

    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)
