import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
server_address = ('localhost', port)
print(f"connecting to server {server_address} port: {port}")
s.connect(server_address)

try:
    filename = "upload.txt"
    f = open(filename,"rb")
    read = f.read(4096)
    f.close()
    read = read.decode()
    msg = "upload "+filename+" "+read
    print("Uploading",filename)
    s.send(msg.encode())

    data = s.recv(4096).decode()
    print(data)

finally:
    print("Close.")
    s.close()
