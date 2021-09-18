from random import randint
from time import sleep
lista = list()
def sorteia():
    global lista
    print("-=" * 20)
    print("Sorteando 5 números: ", end="")
    for i in range(5):
        s = randint(1,10)
        print(f"{s}", end="-")
        sleep(1)
        lista.append(s)
    print("Pronto!")
    soma(lista)
def soma(l):
    s = 0
    for i in l:
        if i % 2 == 0:
            s += i
    print(f"Somando os números pares {l}, temos {s}")
sorteia()



