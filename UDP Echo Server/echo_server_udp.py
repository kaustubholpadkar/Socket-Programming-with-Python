import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9999
server_socket.bind((host, port))

while True:
    message, address = server_socket.recvfrom(1024)
    print('Message received : ' + message.decode())
    server_socket.sendto(message, address)
