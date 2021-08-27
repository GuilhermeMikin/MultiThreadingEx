# Sem criar uma classe

from threading import * 

def show():
    for i in range(6):
        print("Esta é uma Thread filha: ", current_thread().getName())

t = Thread(target = show)
print(current_thread().getName())
t.start()
t.join()
print("Esta é uma Thread mãe: ", current_thread().getName())

