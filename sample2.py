# By extending Thread class

from threading import * 

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("This is a child class:", current_thread().getName())

objt = MyThread()
objt.start()
objt.join()
for i in range(10):
    print("This is the main thread:", current_thread().getName())