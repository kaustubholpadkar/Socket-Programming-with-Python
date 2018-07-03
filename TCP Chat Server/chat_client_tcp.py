import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
client_socket.connect((host, port))

msg = client_socket.recv(1024).decode()
print('Server : ' + msg)

while True:
    print('Client : ', end="")
    msg = input()
    client_socket.send(msg.encode())
    msg = client_socket.recv(1024).decode()
    print('Server : ' + msg)

client_socket.close()
