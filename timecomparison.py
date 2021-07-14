# Multithreading time comparison

from threading import *
import time

def d2(n):
    for x in n:
        time.sleep(1)
        print(x/10)

def d3(n):
    for x in n:
        time.sleep(1)
        print(x*10)

#Without Multithreading
n = [10,20,30,40,50]
s = time.time()
d2(n)
d3(n)
e = time.time()
print(f"Time spent: {round(e-s,2)}s\n")

#With Multithreading
st = time.time()
t1 = Thread(target=d2,args=(n,))
t2 = Thread(target=d3,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
et = time.time()
print(f"Time spent with Multithreading: {round(et-st,2)}s")