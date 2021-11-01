import socket 
import sys
def main():
    try:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as i:
        print(f'ERRO: {i}')
        sys.exit()
    else:
        print('Conexão feita com sucesso')
    host = input('Host~# ')
    porta = int(input('Port~# '))
    try:
        a.connect((host, porta))
    except socket.error as i:
        print(f'ERRO: {i}')
        a.shutdown(2)
    else:
        print('Conexão realizada')


if __name__ == '__main__':
    main()



