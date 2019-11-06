import threading

class Task(threading.Thread):

    def __init__(self, startTime, deadline, priority):
        threading.Thread.__init__(self)
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        self.is_running = False

    def start_task(self):
        self.is_running = True
        threading.Thread.start(self)

    def block_task(self):
        self.is_running = False

    def resume_task(self):
        self.is_running = True
