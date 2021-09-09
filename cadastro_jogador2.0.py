dados = dict()
lista = list()
while True:
    gols = list() # Toda vez que o loop iniciar, será criado uma lista gols
    sg = 0
    dados['name'] = str(input("Name: ")).upper()
    partida = int(input(f"Quantas partidas o {dados['name']} jogou: "))
    if partida >= 1:
        for i in range(partida):
            g = int(input(f"Quantos gols na {i+1}ª partida: ")) 
            sg += g # Soma a quantidade de gols marcados
            gols.append(g)
    dados['gols'] = gols
    dados['total'] = sg
    lista.append(dados.copy())
    while True:
        cont = str(input("Quer continuar: [S/N] ")).upper()[0]
        if cont not in 'SN':
            print("[ERRO], somente S ou N")
            continue
        else:
            break
    del gols # Excluindo a lista para adicionar uma nova
    if cont in 'N':
        break
print("-=" * 20)
print("cod ", end="")
for i in dados.keys():
    print(f"{i:<15} ", end="") # Pegando as chaves(indices) do dicionário
print()
for i, v in enumerate(lista):
    print(f"{i:>3} ", end="") # Colocando o índice três caracteres a esquerda
    for p in v.values():
        print(f"{str(p):<15} ", end="") # Transformando os valores em um string
    print()
while True:
    p = int(input("Quer verificar as estatistica do jogador: (cod) / (444 para sair) "))
    if p == 444:
        break
    if p >= len(lista):
        print("Não tem esse (cod) nas opções")
        continue
    else:
        print(f"\t == ESTATISTICA DO JOGADOR ==> '{lista[p]['name']}'")
        for i, v in enumerate(lista[p]['gols']):
            print(f"\t No {i+1}º jogo marcou {v} gols")
        print()
print("-=" * 20)
print("THANKS. TAKE CARE!")
    
            







    
  


        

    








