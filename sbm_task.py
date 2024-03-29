from time import perf_counter
import time
import socket
import task
import ev3dev.ev3 as ev3


backWheel = ev3.LargeMotor('outA')

#backWheel = ev3.LargeMotor('outA')
globals()['position_sbm'] = 0

class SBMTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start SBM")
        print('The position is:', position_sbm)
        globals()['position_sbm'] = position_sbm - 1000
        backWheel.run_to_abs_pos(position_sp=position_sbm, speed_sp = 200)
        time.sleep(8)
        backWheel.run_to_abs_pos(position_sp=position_sbm, speed_sp = 50)
        time.sleep(3)
        print("Done with SBM")
        self.end_task()
        return