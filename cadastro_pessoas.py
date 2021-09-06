dados = dict()
lista = list()
women = list()
s = m = 0
while True:
    dados['name'] = str(input("Name: "))
    dados['sex'] =  str(input("Sex: [F/M] ")).upper()[0]
    if dados['sex'] not in 'FM': # SE A RESPOSTA FOR DIFERENTE DE "F OU M" ENTRARÁ NO LOOP.
        while True:
            del dados['sex'] # TODA VEZ QUE FOR DIGITADO A OPÇÃO ERRADA, APAGARÁ ESSA OPÇÃO.
            print("Please, only F or M")
            dados['sex'] = str(input("Sex: [F/M] ")).upper()[0]
            if dados['sex'] in 'FM': # OPÇÃO ESTANDO CORRETA, ENTRA NA CONDIÇÃO "IF".
                break # QUEBRA O LOOP.
    if dados['sex'] in 'F':
        women.append(dados['name']) # SERÁ ARMAZENADO OS NOMES DA MULHERES IDENTIFICADA PELO SEXO "F".
    dados['age'] = int(input("Age: "))
    s += dados['age']
    lista.append(dados.copy()) # OS VALORES ARMAZENADOS NO DICIONÁRIO, SERÁ PASSADO PARA A LISTA.

    again = str(input("Do you want to go again: [Y/N] ")).upper()[0]
    if again not in 'YN':
        while True:
            print("[ERROR]: Please, only Y or N:")
            again = str(input("Do you want to go again: [Y/N] ")).upper()[0]
            if again in 'YN':
                break
    else:
        if again in 'N':
            break # QUEBRAR O LOOP WHILE, CASO A RESPOSTA SEJA ENCERRAR O PROGRAMA, E NÃO TENHA NENHUM ERRO NA ESCOLHA 
    if again in 'N': # QUEBRANDO O LOOP WHILE PRINCIPAL, CASO A RESPOSTA SEJA NÃO CONTINUAR.
        break
m = s / len(lista)
print("\033[31m*\033[m" * 30)
print(f"1) Were registered {len(lista)} people")
print(f"2) The average age is {m:5.2f}")
if len(women) >= 1: # SÓ ENTRERÁ NA CONDIÇÃO "IF", SE TIVER MAIS DE UMA MULHER REGISTRADA.
    print("3) The registered women were ", end=" ")
    for i in women:
        print(f"{i} ", end="")
else:
    print("3) No registered women")
print("\n4) People above the middle ages")
for i in lista:
    if i['age'] >= m: # SE A IDADE FOR MAIOR QUE A IDADE MÉDIA, O NOME DA PESSOA SERÁ SELECIONADA.
        for k, v in i.items():
            print(f" {k} = {v} ", end="")
        print()
print("\033[31m*\033[m" * 30)
print("FINISH")


    


