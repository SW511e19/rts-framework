import task
import time
import ev3dev.ev3 as ev3

globals()['position_pcp'] = 0
frontWheel = ev3.LargeMotor('outB')

class PCPTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

    def task_body(self):
        print("Start PCP")
        print('The position is:', position_pcp)
        globals()['position_pcp'] = position_pcp - 50
        frontWheel.run_to_abs_pos(position_sp=position_pcp, speed_sp = 50)
        time.sleep(2)
        print("Done with PCP")
        self.end_task()
        return
