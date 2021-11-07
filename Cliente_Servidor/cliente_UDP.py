import socket 
#Criando a conexão UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente criado com sucesso!!!')

host = 'localhost'
porta = 5493
mensagem = 'Cliente: Olá servidor!!'

try:
    # A mensagem será encapsulada, sendo enviada para um host e uma porta definida.
    s.sendto(mensagem.encode(), (host, 5492))
    # Quantidades de bytes que o servidor deve enviar.
    dados, sevidor = s.recvfrom(4096)
    # O arquivo será desencapsulado.
    dados = dados.decode()
    print(f'{dados}')
finally:
    print('Cliente encerrando a comunicação')
    s.close()