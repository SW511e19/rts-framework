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
            # TODO Add scheduler code
            print("asd")


def get_time_ms():
    return int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)


def is_highest_priority(task_list, task):
    increment = len(task_list)
    while increment > 0:
        increment -= 1
        highest_priority_task = task_list[0]
        for item in task_list:
            if item.priority < highest_priority_task.priority:
                highest_priority_task = item
    # returns null if task_list is empty, error is referenced before assignment
    return highest_priority_task


def has_exceeded_deadline(task):
    deadline = task.startTime() + task.deadline
    return deadline > get_time_ms


def remove_task(task_list, task):
    task_list.remove(task)
    return sorted(task_list, key=lambda task: task.priority, reverse=True)


def append_task(task_list, task):
    task_list.append(task)
    return sorted(task_list, key=lambda task: task.priority, reverse=True)


# Priority is scheduled from incrementally, from 100 being the lowest and 500 being the highest.
# TODO : Add each at the end of each task.
# Back Wheel Task (multiple cards)
BCW = bcw_task.BCWTask(get_time_ms, 1000, 500)
OCW = ocw_task.OCWTask(get_time_ms, 1000, 400)  # Front Wheel Task (one card)
PPC = ppc_task.PPCTask(get_time_ms)  # Communication wth Raspberry Pi
PCP = pcp_task.PCPTask(get_time_ms, 1000, 200)  # Piston to push the card
SBM = sbm_task.SBMTask(get_time_ms, 1000, 100)  # Sliding the box in position
asd = bcw_task.BCWTask(get_time_ms, 1000, 5000)  # test
asd2 = bcw_task.BCWTask(get_time_ms)  # test

# Add all the Tasks to a list, in the order of the highest being the first to be ran (highest priority) - may as well
# sort it manually
task_list = [SBM, PCP, PPC, OCW, asd, asd2, BCW]

# Sets the default task to be the lowest
active_task = SBM
while True:
    print("active_task : " + str(active_task))
    # check if SBM is the highest priority -> Yes
    task_to_run = is_highest_priority(task_list, active_task)
    if active_task != task_to_run:
        print("SBM is not the highest prio anymore")
        active_task = task_to_run

    if active_task == task_to_run:
        print("Active Task is the highest prio")
        # Check if the deadline has exceeded, kills the thread if it has
        # Run the tasks if it is not running
        if not active_task.is_running:
            if active_task.task_completed:
                task_list = remove_task(task_list, active_task)
            active_task.start_task()

    time.sleep(1)
