import socket 
# Criando a conexão UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Servidor criado com sucesso')

host = 'localhost'
porta = 5492

# Verificando ser existe alguma conexão entre o host e a porta especificada.
s.bind((host, porta))
mensagem = '\nServidor: Olá cliente!!'

while 1:
    # Quantidades de bytes para ser recebido e também enviado.
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando a mensagem')
        # A mensagem será encapsulada e enviada. 
        s.sendto(dados + (mensagem.encode()), end)
