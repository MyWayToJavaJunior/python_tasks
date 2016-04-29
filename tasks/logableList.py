#!/usr/bin/python3


import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ':' + str(msg))


class LoggableList(list, Loggable):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)


c = LoggableList()
c.append(1)
print(c)
print(c)
