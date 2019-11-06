import threading

class Scheduler(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def isHighestPriority(task_list, task):
        increment = len(task_list)
        while (increment > 0):
            increment -= 1
            highest_prio_task = task_list[0]
            for item in task_list:
                if item.priority < highest_prio_task.priority:
                    highest_prio_task = item
        return highest_prio_task