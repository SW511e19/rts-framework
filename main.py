import task
import bcw_task
import ocw_task
import ppc_task
import pcp_task
import sbm_task
import datetime
import threading
import time
import copy


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)

def isHighestPriority(task_list, task):
    increment = len(task_list)
    while (increment > 0):
        increment -= 1
        highest_prio_task = task_list[0]
        for item in task_list:
            if item.priority < highest_prio_task.priority:
                highest_prio_task = item
    return highest_prio_task
    

# Priority is scheduled from incrementally, from 100 being the lowest and 500 being the highest.
# TODO : Add each at the end of each task.
BCW = bcw_task.BCW_Task(get_time_ms, 1000, 500)  # Back Wheel Task (multiple cards)
OCW = ocw_task.OCW_Task(get_time_ms, 1000, 400)  # Front Wheel Task (one card)
PPC = ppc_task.PPC_Task(get_time_ms)  # Communication wth Raspberry Pi
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

# Sets the default task to be the lowest
active_task = SBM

# check if SBM is the highest prio -> Yes
task_to_run = isHighestPriority(task_list, SBM)
if (SBM != task_to_run):
    print("SBM is not the highest prio anymore")
if (SBM == task_to_run):
    print("SBM is the highest prio")
    
# SBM ran
task_list.remove(SBM)

# Resorting Priorities
task_list = sorted(task_list, key=lambda task: task.priority, reverse=True)

# check if SBM is the highest prio -> No
task_to_run = isHighestPriority(task_list, SBM)
if (SBM != task_to_run):
    print("SBM is not the highest prio anymore")
    print("The Highest Priority is : ")
    print(task_to_run)
if (SBM == task_to_run):
    print("SBM is the highest prio")
    