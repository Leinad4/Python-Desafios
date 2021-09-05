from random import randrange
from operator import itemgetter
from time import sleep
info = dict()
for i in range(1, 5): # Haverá um sorteio para os 4 NPCs
    dado = randrange(1, 6)
    print(f"Player {i}: {dado} points")
    info.setdefault(f"Player {i}", dado) # Será adicionado no dicionário
ranking = list()
ranking = sorted(info.items(), key=itemgetter(1), reverse=True) # Os valores e as chaves(indice) serão colocados do maior para o menor
print("*" * 20)
print("    <-RANKING->")
print("*" * 20)
for i, v in enumerate(ranking): 
    print(f"{i+1}st place: {v[0]} with {v[1]} points")
