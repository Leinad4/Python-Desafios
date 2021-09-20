from datetime import datetime 
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        print(f"Você tem {idade} anos. VOTO NEGADO!")
    elif idade >= 16 and idade < 18:
        print(f"Você tem {idade} anos. VOTO OPCIONAL!")
    elif idade >= 18 and idade < 60:
        print(f"Você tem {idade} anos. VOTO OBRIGATÓRIO!")
    else:
        print(f"Você tem {idade} anos. VOTO OPCIONAL!")
    
   
a = int(input("Dígite sua data de nascimento: "))
voto(a)
