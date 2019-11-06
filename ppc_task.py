import task
import datetime
import threading


class PPC_Task(task.Task):
    def __init__(self, startTime, deadline=1000, priority=9000):
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        self.is_running = False
