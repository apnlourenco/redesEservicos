import socket

HOST = 'localhost'
PORT = 5000

def start_server(address: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #create INET(pega o IP da maquina) streaming socket(escolhe o tipo tcp) = TCP

    server_socket.bind((address, port))
    server_socket.listen(1)

    print('Server rodando..')
    while True:
        client, address = server_socket.accept()
        #handshake - syn, ack 

        print(f'Conexão aceita no endereço {address}')
        data = client.recv(1024)
        #recebe a mensagem que o cliente ta enviando, 1024 é o numero de bytes

        print(f'Menssagem: {data.decode()}')
        client.send('Mensagem recebida!'.encode())
        client.close()

if __name__ == "__main__":
    start_server(HOST, PORT)