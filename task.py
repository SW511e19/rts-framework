import threading


class Task(threading.Thread):
    is_running = False
    killThread = False
    task_completed = False

    def __init__(self, startTime, deadline, priority):
        threading.Thread.__init__(self)
        self.startTime = startTime
        self.deadline = deadline
        self.priority = priority
        threading.Thread.start(self)

    # the driver for each task, overwritten from Thread.run
    def run(self) -> None:
        while True:
            while self.is_running:
                self.task_body()
                print("Task Completed")
                if self.killThread:
                    print("Task killed")
                    return
                return

    # method used by tasks to do their work
    # should be overwritten in inheriting classes
    def task_body(self):
        # no implementation in super class
        return

    # method for stopping a task
    def start_task(self):
        self.is_running = True

    # method for stopping a task
    def end_task(self):
        self.is_running = False
        self.task_completed = True

    def killThread(self):
        self.killThread = True
