import random, time
vida = 3
item = ['PEDRA', 'PAPEL', 'TESOURA']
resp = 'S'
jogador = 0
cv = 0
cd = 0
ce = 0

while resp != 'N':

    #Apresentando as opções de possíveis jogadas
    print(f"""
    \033[36m+=================================+\033[m
    \033[36m+ ***********    **************   +\033[m
    \033[36m+ #\033[m \033[35mVIDA:\033[m \033[33m{vida}\033[m \033[36m#\033[m    \033[36m#\033[m \033[35mVITÓRIA: \033[33m{cv}\033[m \033[36m#   +\033[m 
    \033[36m+ ***********    **************   +\033[m 
    \033[36m+ ******************************* +\033[m
    \033[36m+ *\033[m         \033[37mJO-KEN-PÔ\033[m           \033[36m*\033[m \033[36m+\033[m
    \033[36m+ ******************************* +\033[m
    \033[36m+\033[m \033[37mESCOLHA UMA DAS OPÇÕES:\033[m         \033[36m+\033[m
    \033[36m+ [\033[m\033[32m0\033[m\033[36m]\033[m\033[31mPEDRA\033[m  \033[36m[\033[m\033[32m1\033[m\033[36m]\033[m\033[31mPAPEL\033[m  \033[36m[\033[m\033[32m2\033[m\033[36m]\033[m\033[31mTESOURA\033[m  \033[36m+\033[m
    \033[36m+=================================+\033[m""")

    computador = random.randrange(0, 2) #O computador escolherá randomicamente um número de 0 até 2
    
    jogador = int(input("Qual é a sua jogada: "))
    if jogador < 0 or jogador > 2:
        print("Opção não encontrada")
        continue
    print("\033[31mJO\033[m")
    time.sleep(1)
    print("\033[31mKEN\033[m")
    time.sleep(1)
    print("\033[31mPÔ\033[m")
    time.sleep(0.5)
    print(f"Você escolheu \033[34m{item[jogador]}\033[m") #Escolhendo um número que identificará um índice dentro da lista item 
    print(f"Computador jogou \033[33m{item[computador]}\033[m")

    if computador == 0:
        if jogador == 0:
            print("""
            +=========+
            +  EMPATE +
            +=========+""")
            ce += 1
        if jogador == 1:
            print("""
            +=========+
            + VITÓRIA +
            +=========+""")
            cv += 1 #Conta toda vez que o jogador ganha
        if jogador == 2:
            print("""
            +=============+
            + VOCÊ PERDEU +
            +=============+""")
            vida -= 1 #Tira um ponto de vida do jogador
            cd += 1
    if computador == 1:
        if jogador == 0:
            print("""
            +=============+
            + VOCÊ PERDEU +
            +=============+""")
            vida -= 1
            cd += 1
        if jogador == 1:
            print("""
            +=========+
            +  EMPATE +
            +=========+""")
            ce += 1
        if jogador == 2:
            print("""
            +=========+
            + VITÓRIA +
            +=========+""")
            cv += 1
    if computador == 2:
        if jogador == 0:
            print("""
            +=========+
            + VITÓRIA +
            +=========+""")
            cv += 1
        if jogador == 1:
            print("""
            +=============+
            + VOCÊ PERDEU +
            +=============+""")
            vida -= 1
            cd += 1
        if jogador == 2:
            print("""
            +========+
            + EMPATE +
            +========+""")
            ce += 1
    if cv == 5: #Jogador ganhando 5 vezes, é adicionado 1 ponto de vida ao jogador
        print(f"{cv} vitórias consecutivas. Ganhou 1 ponto de vida")
        vida += 1
        cv = 0 #Adicionando 1 ponto de vida, o placa de vitórias vai ser zerado
    if vida >= 3: #A vida não pode passar de três pontos
        vida = 3
    if vida == 0: # Se a vida do jogador chegar a zero, game over
        print("\033[31mGAME OVER\033[m")
        break    
    resp = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
print(f"""
+====================+
+ VENCEU {cv} VEZES  
+ PERDEU {cd} VEZES  
+ EMPATE {ce} VEZES  
+====================+
+ OBRIGADO POR JOGAR +
+====================+       
""")

    
    