from threading import *
import time

start = time.perf_counter()


threads = []


def do_something(seconds):
    print(f'Dormindo {seconds} segundo(s)...')
    time.sleep(seconds)
    print('Parou de dormir...')


for _ in range(10):
    t = Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 2)} segundo(s).')