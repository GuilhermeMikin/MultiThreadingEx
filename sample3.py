# Sem estender uma classe Thread

from threading import * 

class Demo:
    def show(self):
        lst = [1,2,3,4,5,6,7,8,9,10]
        for i in lst:
            print(f"Classe filha printando {i} na {current_thread().getName()}")
obj=Demo()
t=Thread(target=obj.show) 
t.start()
t.join() #tente comentar "t.join() e adicionar () ao "obj.show" target
for i in range(10):
    print("Esta é a Thread mãe", current_thread().getName())
