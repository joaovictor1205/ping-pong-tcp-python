import socket              

s = socket.socket()
host = socket.gethostname()
port = 8081
s.bind((host, port))

print('Esperando conexão.')
s.listen(5)             

while True:
   clientsocket, address = s.accept()

   while True:
       print('Esperando mensagem.')                         # Establish connection with client.
       message = clientsocket.recv(1024).decode('utf8')

       if message == 'SAIR':
           print('Conexão encerrada.')
           break

       print('Mensagem recebida: ' + message)
       reply = input('Digite resposta: ')
       clientsocket.send(bytes(reply, encoding='utf8'))
       print('Resposta enviada.')

   clientsocket.close()   