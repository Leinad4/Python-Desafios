import moeda
preco = float(input("Dígite o preço:R$ "))
taxa = str(input("Tem taxa: Y/N ")).upper()[0]
if taxa in 'Y':
    t = int(input("Qual é o valor da taxa: "))
print(f"A metade de R${preco:5.2f} é R${moeda.metade(preco):5.2f}")
print(f"O dobro de R${preco:5.2f} é R${moeda.dobro(preco):5.2f}")
if taxa in 'Y':
    print(f"Com um aumento de {t}%, temos R${moeda.aumento(preco, t):5.2f}")
