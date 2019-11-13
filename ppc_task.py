import task
#import scheduler
import time
import pcp_task
import datetime
import socket

globals()['position_ppc'] = 0
# Settings Up
msgFromClient = "READY"
bytesToSend = str.encode(msgFromClient)
bufferSize = 1024
serverAddressPort = ("172.28.210.59", 22222) # IP and Port of the Raspberry PI

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

class PPCTask(task.Task):
    def __init__(self, startTime, deadline=1000, priority=1337):
        super().__init__(startTime, deadline, priority)
        
    def task_body(self):
        print("Start PPC")
        print('The position is:', position_ppc)
        globals()['position_ppc'] = position_ppc + 1000
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Upcode from the Rasberry Pi {}".format(msgFromServer[0])
        print(msg)
        time.sleep(15)
        if ("card" in msg):
            print("Pushed Piston")
        if ("not_card" in msg):
            #frontMotor(position)
            #position = position - 60
            print("Done with PPC")
        self.end_task()
        return
