import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
server_address = ('localhost', port)
print(f"connecting to server {server_address} port: {port}")
s.connect(server_address)

try:
    command = "list"
    s.send(command.encode())
    data = s.recv(2048)
    d = data.decode()
    print(d)
finally:
    s.close()


