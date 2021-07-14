# Without creating a class

from threading import * 

def show():
    for i in range(6):
        print("This is a child thread:", current_thread().getName())

t = Thread(target = show)
print(current_thread().getName())
t.start()
t.join()
print("This is parent thread:", current_thread().getName())

