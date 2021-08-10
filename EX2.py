#O Programa irá retornar ao usuário o termino de uma palestra
#Pedindo as informações ao usuário
hora = int(input("Quantas horas: ")) 
minutos = int(input("Quantos minutos: "))
termino = int(input("Qual é a duração da palestra: "))

#Transformando as informações em dados

nv_hora = (termino + minutos) // 60 #Separando o resultado da divisão inteira   
hora_agora = (nv_hora + hora) % 24 #Somando o resultado da divisão inteira com a hora informada pelo usuário e, tirando o resto da divisão por 24 (zera quando chega no 24 recomeçando) 
minuto_agora = (termino + minutos) % 60 #Somando e retirando o resto de 60 (60 minutos), que será os novos minutos

#Retornando ao usuário as horas que a palestra terminará
print(f"{hora_agora}:{round(minuto_agora, 2)}")
