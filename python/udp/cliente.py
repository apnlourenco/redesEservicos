import socket

def start_client(address: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #create INET(pega o IP da maquina) data gram socket(escolhe o tipo udp) = UDP
    #aceita varias conexoes
    server_socket.connect((address, port))

    while True:
        message = input('Digite uma mensagem: ').encode()

        #message = 'Uma mensagem qualquer'.encode()
        server_socket.connect((address, port))
        server_socket.sendto(message, (address, port))
        data = server_socket.recvfrom(1024)
        print(f'Mensagem do servidor: {data.decode()}')


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 8000

    start_client(HOST, PORT)