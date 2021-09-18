from time import sleep
def maior(*num):
    maior = 0
    print("-=" * 20)
    print("Analisando os valores passados...")
    for i in num:
        print(f"{i}", end="-")
        sleep(0.5)
    print("Fim!")
    for i in num:
        if i > maior:
            maior = i
    if maior == 0:
        print("Zeradinho") 
    else:   
        print(f"MAIOR: {maior}")
maior(9, 2, 102,1)
maior(4, 2, 9, 1)
maior()

       


        

