import task
import time

globals()['position_pcp'] = 0

class PCPTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start PCP")
        print('The position is:', position_pcp)
        globals()['position_pcp'] = position_pcp + 1000
        print("Done with PCP")
        self.end_task()
        return
