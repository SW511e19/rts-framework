import task
import time


class OCWTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start OCW")
        time.sleep(3)
        print("Done with OCW")
        self.end_task()
        return
