#Você quer viajar para o exterior, mas não sabe como converter o seu dinheiro:
#Primeiro informe a quantia:
dinheiro = float(input("Quanto você quer converter: R$ ")) #Baseando que a origem do dinheiro seja reais
cotacao = float(input("Qual é a cotação hoje: ")) #Valor do real no dia de hoje
dolar = dinheiro * cotacao #Vamos converter para dolar
print("US${:.2f} dolares".format(dolar))
