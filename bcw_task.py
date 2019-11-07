import task


class BCW_Task(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        super().__init__(startTime, deadline, priority)
    
    def task_body(self):
      #TODO not yet implemented
      return