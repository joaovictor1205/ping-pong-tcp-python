import socket

s = socket.socket()
host = socket.gethostname()
port = 8081

s.connect((host, port))

while True:

    message = input('Digite mensagem: ')
    s.send(bytes(message, encoding='utf8'))

    if message == 'SAIR':
        break

    print('Mensagem enviada.')
    print('Esperando resposta.')
    answer = s.recv(1024).decode('utf8')
    print('Resposta recebida: ' + answer)

print('Desconectando.')
s.close()