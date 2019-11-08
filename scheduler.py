import threading
import datetime
import bcw_task
import ocw_task
import pcp_task
import ppc_task
import sbm_task
import time


class Scheduler(threading.Thread):
    def __init__(self, task_lst):
        self.task_lst = task_lst
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self) -> None:
        while True:
            # timeslice(self.task_lst)
            print("asd")


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


def hasExceededDeadline(task):
    deadline = task.startTime() + task.deadline
    return deadline > get_time_ms


def taskDone(task_list, task):
    task_list.remove(task)
    task_list = sorted(task_list, key=lambda task: task.priority, reverse=True)
    return task_list


def taskAppend(task_list, task):
    task_list.append(task)
    task_list = sorted(task_list, key=lambda task: task.priority, reverse=True)
    return task_list


# Priority is scheduled from incrementally, from 100 being the lowest and 500 being the highest.
# TODO : Add each at the end of each task.
# Back Wheel Task (multiple cards)
BCW = bcw_task.BCW_Task(get_time_ms, 1000, 500)
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
while (True):
    print("active_task : " + str(active_task))
    # check if SBM is the highest prio -> Yes
    task_to_run = isHighestPriority(task_list, active_task)
    if (active_task != task_to_run):
        print("SBM is not the highest prio anymore")
        active_task = task_to_run

    if (active_task == task_to_run):
        print("Active Task is the highest prio")
        # Check if the deadline has exceeded, kills the thread if it has
        # Run the tasks if it is not running
        if (not active_task.is_running):
            if (active_task.task_completed == True):
                task_list = taskDone(task_list, active_task)
            active_task.start_task()

    time.sleep(1)
