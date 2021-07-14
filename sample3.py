# Without extending Thread class

from threading import * 

class Demo:
    def show(self):
        for i in range(10):
            print("This is the child class")
obj=Demo()
t=Thread(target=obj.show())
t.start()
for i in range(10):
    print("This is the parent thread")
