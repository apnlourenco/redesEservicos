import socket

def start_client(address: str, port: int):
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #create INET(pega o IP da maquina) streaming socket(escolhe o tipo tcp) = TCP
    message = input('Digite uma mensagem: ').encode()

    #message = 'Uma mensagem qualquer'.encode()
    client_server.connect((address, port))
    client_server.sendall(message)
    data = client_server.recv(1024)
    print(f'Mensagem do servidor: {data.decode()}')


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 8000

    start_client(HOST, PORT)