# Without creating a class

from threading import * 

def show():
    print("This is a child thread")
t = Thread(target = show())
t.start()
print("This is parent thread")

