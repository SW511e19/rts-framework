import task
import time

globals()['position_bcw'] = 0

class BCWTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start BCW")
        print('The position is:', position_bcw)
        globals()['position_bcw'] = position_bcw + 1000
        print("Done with BCW")
        self.end_task()
        return
