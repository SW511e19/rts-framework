import task
import time


class SBM_Task(task.Task):
    
    def task_body(self):
      print("Start SBM")
      time.sleep(3)
      print("Done with SBM")
      self.end_task()
      return

  
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)