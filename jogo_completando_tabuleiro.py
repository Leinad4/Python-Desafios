from random import choice, randint  
from time import sleep
matriz = []
print("""
+===========================================+
+       BEM VINDO AO JOGO DOS 15 NÚMEROS    +
+===========================================+
""")

# Parte principal do programa 
def main():
    global matriz
    while True:
        jogar = int(input("[1] JOGAR [2] SAIR "))
        if jogar == 1:
            matriz.clear()
            inicio()
        else:
            print("Até mais. Tchau")
            break
    exit()

# Controle do jogador 
def inicio():
    global matriz
    gerandoMatriz(matriz)
    while True:
        Tabela(matriz)
        
        p1 = int(input(" 1º [linha][coluna]: "))
        p2 = int(input(" 2º [linha][coluna]: "))
        troca(p1, p2, matriz) # Mecanismos de trocar dos números 

        r = int(input("Está concluido: [1] SIM [2] NÃO "))
        if r == 1:
            venceu(matriz) # Verifica se a tabela está correta 
        if r != 1 and r != 2:
            print("Não tem essa opção: Continuemos então")
            continue
        if r == 2:
            continue
# A função aleatoriamente adicionará os números na matriz
def gerandoMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):

            x = choice(lista)
            linha.append(x)
            lista.remove(x)
          
        matriz.append(linha)
# A tabela do jogo com os números aleatórios de 0 até 15
def Tabela(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                matriz[i][j] = 'X'
            print(f"\t[{matriz[i][j]:^5}]", end="")
        print()
# A troca dos números na matriz acontece nessa função
def troca(pos1, pos2, matriz):
    
    while True:
        e1 = matriz[pos1//10-1][pos1%10-1]
        e2 = matriz[pos2//10-1][pos2%10-1]
        if e1 == 'X' or e2 == 'X':
            matriz[pos1//10-1][pos1%10-1] = e2
            matriz[pos2//10-1][pos2%10-1] = e1
            break
        else:
            return emergencia() # Um alerta, caso o jogador escolha um número ao invés do 'X'
    for i in range(4):
        for j in range(4):
            print(f"\t[{matriz[i][j]:^5}]", end="")
        print()
    return matriz
def emergencia():

    print("\033[31mNão é permitido mudar para uma posição que já contenha um número\033[m")
    print("\033[31mUtilize o espaço marcado com o X para mudar a posição\033[m")
    sleep(3)
    return inicio()
# Será verificado se a tabela está completa com os números 1 até 15
def venceu(matriz):
    linha = []
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'X']
    for i in range(4):
        for j in range(4):
            linha.append(matriz[i][j])
    
    if linha == lista:
        print("Você venceu. Parabéns!")
        main()
        
    if matriz != lista:
        print("Você perdeu")
        main()
main()








