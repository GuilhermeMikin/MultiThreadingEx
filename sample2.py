# Estendendo uma classe Thread 

from threading import * 

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Essa é uma classe filha: ", current_thread().getName())

objt = MyThread()
objt.start()
objt.join()
for i in range(10):
    print("Esta é a Thread principal: ", current_thread().getName())