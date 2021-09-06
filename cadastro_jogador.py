dados = dict()
dados['Nome'] = str(input("Nome do jogador: "))
partida = int(input(f"Quantas partidas {dados['Nome']} jogou: "))
lista = list()
for i in range(partida):
    gol = int(input(f"Quantos gols na {i+1} partida: "))
    lista.insert(i, gol)
total = 0
for o in lista:
    total += o  
dados['gols'] = lista
dados['total'] = total
print("-=" * 30)
print(dados)
print("-=" * 30)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {dados['Nome']} jogou {partida} partidas")
for i, v in enumerate(lista):
    print(f" => Na partida {i+1} fez {v} gols")
print(f"Foi um total de {dados['total']} gols")

