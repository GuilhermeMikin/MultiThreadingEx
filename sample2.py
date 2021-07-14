# By extending Thread class

from threading import * 

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("This is a child class")

t = MyThread()
t.start()
for i in range(10):
    print("This is the main thread")