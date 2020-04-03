import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
server_address = ('localhost', port)
print(f"connecting to server {server_address} port: {port}")
s.connect(server_address)

try:
    filename = "download.txt"
    msg = "download " + filename
    print("Mendownload ",filename)
    s.send(msg.encode())

    data = s.recv(4096)
    f = open("file/"+filename, "wb")
    f.write(data)
    f.close()
    print("Download success")
finally:
    print("Close.")
    s.close()