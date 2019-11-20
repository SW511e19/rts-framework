import task
import time

globals()['position_ocw'] = 0

class OCWTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start OCW")
        print('The position is:', position_ocw)
        globals()['position_ocw'] = position_ocw + 1000
        time.sleep(3)
        print("Done with OCW")
        self.end_task()
        return
