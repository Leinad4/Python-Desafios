import moeda
v = float(input("Dígite um valor: "))
t = int(input("Dígite a taxa: "))
print(f"A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}")
print(f"O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}")
print(f"Com uma taxa de {t}% houve um aumento de {moeda.aumento(v, t, True)}")
