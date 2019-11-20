from time import perf_counter
import time
import socket
import task



#backWheel = ev3.LargeMotor('outA')
globals()['position_sbm'] = 0

class SBMTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        self.end_task()
        return