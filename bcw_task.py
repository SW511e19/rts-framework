import task
import time


class BCWTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start BCW")
        time.sleep(3)
        print("Done with BCW")
        self.end_task()
        return
