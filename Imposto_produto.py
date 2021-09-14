def somaImposto(taxa_Imposto, custo):
    Imposto_vendas = (taxa_Imposto / 100) * custo # A equação para descobrir o total do imposto sobre o produto
    custo_total = Imposto_vendas + custo # Somando o valor do imposto sobre o custo antes do imposto
    print(f"O custo total do produto já incluido o imposto é de ${custo_total:5.2f} dolares")
ip = float(input("Qual porcentagem do imposto sobre o produto: ")) 
vp = float(input("Valor do produto antes do imposto:$ "))
somaImposto(ip, vp)

