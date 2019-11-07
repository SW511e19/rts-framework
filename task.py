import threading


class Task(threading.Thread):
  
    # method used by tasks to do their work
    # should be overwritten in inheriting classes
    def task_body(self):
        # not implemented in super class
        return

    def __init__(self, startTime, deadline, priority):
        threading.Thread.__init__(self)
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        self.is_running = False
        self.killThread = False
        threading.Thread.start(self)
        

    # the driver for each task, overwritten from Thread.run
    def run(self) -> None:
        while (True):
            while (self.is_running):
                task_body(self)
                print("task completed")
                if (killThread == True):
                  return
                return

    # method for stopping a task
    def start_task(self):
        self.is_running = True
        
    def killThread(self):
      self.killThread = True
