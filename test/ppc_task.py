import task
#import scheduler
import time
import pcp_task
import datetime
import socket

globals()['position_ppc'] = 0
# Settings Up

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

class PPCTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=1337):
        super().__init__(startTime, deadline, priority)
        
    def task_body(self):
        self.end_task()
        return
