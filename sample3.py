from threading import * 

class Demo:
    def show(self):
        for i in range(20):
            print("This is the child class")
obj=Demo()
t=Thread(target=obj.show())
t.start()
for i in range(20):
    print("This is the parent thread")
