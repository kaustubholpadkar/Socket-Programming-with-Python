import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
client_socket.connect((host, port))

while True:
    print('Enter msg : ')
    msg = input()
    client_socket.send(msg.encode())
    print(client_socket.recv(1024).decode())

client_socket.close()
