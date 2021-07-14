# Without extending Thread class

from threading import * 

class Demo:
    def show(self):
        lst = [1,2,3,4,5,6,7,8,9,10]
        for i in lst:
            print(f"This is the child class printing {i} in the {current_thread().getName()}")
obj=Demo()
t=Thread(target=obj.show) #try "obj.show()"
t.start()
t.join() #try commenting the "t.join() and adding () to the "obj.show" target
for i in range(10):
    print("This is the parent thread", current_thread().getName())
