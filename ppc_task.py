import task
import time

globals()['position_ppc'] = 0

class PPCTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=1337):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start PPC")
        print('The position is:', position_ppc)
        globals()['position_ppc'] = position_ppc + 1000
        print("Done with PPC")
        self.end_task()
        return
