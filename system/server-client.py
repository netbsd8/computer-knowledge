import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))

import socket
import select

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8080))
server_socket.listen()

# Set up the epoll object
epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

try:
    connections = {}
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            # New connection
            if fileno == server_socket.fileno():
                client_socket, client_address = server_socket.accept()
                epoll.register(client_socket.fileno(), select.EPOLLIN)
                connections[client_socket.fileno()] = client_socket
            # Data to read
            elif event & select.EPOLLIN:
                client_socket = connections[fileno]
                data = client_socket.recv(1024)
                if data:
                    client_socket.send(data)
                else:
                    # Connection closed
                    epoll.unregister(fileno)
                    client_socket.close()
                    del connections[fileno]
finally:
    epoll.unregister(server_socket.fileno())
    epoll.close()
    server_socket.close()
