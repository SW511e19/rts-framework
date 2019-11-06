import task
import datetime
import time
import threading


class BCW_Task(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        threading.Thread.__init__(self)
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        self.is_running = False

    def run(self):
        asd = 0
        while True:
            self.can_run.wait()
            try:
                self.thing_done.clear()
                asd += 1
                print(asd)
                time.sleep(1)
            finally:
                self.thing_done.set()


    def pause(self):
        self.can_run.clear()
        self.thing_done.wait()


    def resume(self):
        self.can_run.set()
