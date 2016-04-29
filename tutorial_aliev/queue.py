#!/usr/bin/python3


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
q = Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.is_empty())
q.enqueue(8.4)
print(q.dequeue())
print(q.dequeue())
print(q.size())
"""


# горячая картошка

def hot_potato(namelist, num):
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

# print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))

# очередь на печать

import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp



def simulation(num_seconds, pages_per_minute):

    labprinter = Printer(pages_per_minute)
    print_Queue = Queue()
    waitingtimes = []

    for current_second in range(num_seconds):

      if new_printTask():
         task = Task(current_second)
         print_Queue.enqueue(task)

      if (not labprinter.busy()) and (not print_Queue.is_empty()):
        nexttask = print_Queue.dequeue()
        waitingtimes.append(nexttask.wait_time(current_second))
        labprinter.start_next(nexttask)

      labprinter.tick()

    average_wait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait,print_Queue.size()))

def new_printTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)
