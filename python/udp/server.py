import socket

def start_server(address: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #create INET(pega o IP da maquina) data gram socket(escolhe o tipo udp) = UDP
    #aceita varias conexoes

    server_socket.bind((address, port))
    print(f'UDP server listening on {address}:{port}')

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f'Message: {data}')
        #server_socket.sendto(("Mensagem Recebida!".encode(), address))


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 8000

    start_server(HOST, PORT)
