def ficha(nome="<desconhecido>", gols=0):
    if nome != "<desconhecido>" and gols != 0:
        print(f"O jogador {nome} marcou {gols} gol(s)")
    elif nome == "<desconhecido>" and gols != 0:
        print(f"O jogador {nome} marcou {gols} gol(s)")
    elif nome != "<desconhecido>" and gols == 0:
        print(f"O jogador {nome} marcou {gols} gol(s)")
    else:
        print(f"O jogador {nome} marcou {gols} gol(s)")
n = str(input("Dígite o nome do jogador: "))
g = str(input("Dígite um números de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == "":
    ficha(nome="<desconhecido>", gols=g)
else:
    ficha(n, g)