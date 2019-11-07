import threading
import time

class Task(threading.Thread):

    def __init__(self, startTime, deadline, priority):
        threading.Thread.__init__(self)
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        self.is_running = True
        threading.Thread.start(self)
      
    def run(self) -> None:
      while (True):
        while (not self.is_running):
          #Do stuff here
          print("done")
          return

    def stop_task(self):
      self.is_running = False

class OCW_Task(Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)

import datetime
import time
def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)

#OCW = OCW_Task(get_time_ms, 1000, 400)  # Front Wheel Task (one card)
#OCW.test()
qwe = Task(get_time_ms, 1000,400)
qwe.test()
