import task
import bcw_task
import ocw_task
import ppc_task
import pcp_task
import sbm_task
import datetime
import threading
import time


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


# Priority is scheduled from incrementally, from 100 being the lowest and 500 being the highest.
# TODO : Add each at the end of each task.
BCW = bcw_task.BCW_Task(get_time_ms, 1000, 500)  # Back Wheel Task (multiple cards)
OCW = ocw_task.OCW_Task(get_time_ms, 1000, 400)  # Front Wheel Task (one card)
PPC = ppc_task.PPC_Task(get_time_ms, 1000, 300)  # Communication wth Raspberry Pi
PCP = pcp_task.PCP_Task(get_time_ms, 1000, 200)  # Piston to push the card
SBM = sbm_task.SBM_Task(get_time_ms, 1000, 100)  # Sliding the box in position
asd = bcw_task.BCW_Task(get_time_ms, 1000, 5000)  # test
asd2 = bcw_task.BCW_Task(get_time_ms)  # test

# Add all the Tasks to a list, in the order of the highest being the first to be ran (highest priority) - may as well sort it manually
task_list = []
task_list.append(SBM)
task_list.append(PCP)
task_list.append(PPC)
task_list.append(OCW)
task_list.append(asd)
task_list.append(asd2)
task_list.append(BCW)

# Looks through the list of tasks, finds the task with highest priority and will run the one with highest
# Target will be time slice on 1 seconds will be implemented and execute 
while (len(task_list) > 0):
    highest_prio_task = task_list[0]
    for item in task_list:
        if item.priority < highest_prio_task.priority:
            highest_prio_task = item
    task_list.remove(highest_prio_task)  # to be set to run instead of remove"
    print(highest_prio_task.priority)
    
asd.run()
time.sleep(5)
print("Stopped sleeping")
asd.pause()
print("paused and sleeping for 10 sec")
time.sleep(10)
print("resumed")
asd.resume()
