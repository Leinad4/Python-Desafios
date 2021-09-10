def ano(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0: # Verificando se é um ano bissexto
        return True # Se for um ano bissexto 
    else:
        False # Não é um ano bissexto
     

dado = [1900, 2000, 2016, 1987]
test = [False, True, True, False]
for i in range(len(dado)): # Percorrendo a lista de ano
    x = dado[i]
    print(x, "->", end="")
    resu = ano(x) # Chamando a função
    if resu == test[i]:
        print("Ok")
    else:
        print("Failed")
