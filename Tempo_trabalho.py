dados = dict()
dados['name'] = str(input("Name: "))
dados['idade'] = int(input('How old are you: '))
dados['data'] = str(input("Do you work: [y/n] "))
if dados['data'] in 'Yy':
    dados['year'] = int(input("When do you started work: (year) "))
    dados['cash'] = float(input("How much was your salary: "))
    dados['time_work'] = ((dados['idade'] + 35) - 1)
print("-=" * 20)
print(' +++++ Workers ++++++')
print("-=" * 20)
for i, v in enumerate(dados.items()):
    print(f"{v[0]}: {v[1]}")