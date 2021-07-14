# Multithreading

from threading import *
from time import sleep

class Demo:

    def num(self):
        for i in range(1, 6):
            print(f"The number is {i}")
            sleep(1)
    
    def double(self):
        for i in range(1, 6):
            print("The double of the number is ", 2*i)
            sleep(1)

    def square(self):
        for i in range(1,6):
            print(f"The square of the number is {i*i}")
            sleep(1)

obj = Demo()
# obj.num()
# obj.double()
# obj.square()
t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
sleep(0.2)
t2.start()
sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print("This is the main thread..")