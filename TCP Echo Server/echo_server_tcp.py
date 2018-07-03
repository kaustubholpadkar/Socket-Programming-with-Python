import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
server_socket.bind((host, port))

server_socket.listen(1)

connection, address = server_socket.accept()

while True:
    msg = connection.recv(1024).decode()
    print('Message received : ' + msg)
    connection.send(msg.encode())
