import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 9999
server_address = (host, port)

while True:
    print('Enter msg : ')
    message = input()
    client_socket.sendto(message.encode(), server_address)
    message, address = client_socket.recvfrom(1024)
    print(message.decode())

client_socket.close()
