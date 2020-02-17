import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

with open("send.txt","rb") as f:
    #send file
    print("Sending file ...")
    send_data = f.read()
    sock.sendall(send_data)
    
    sock.close()
    print("Disconnected")
    sys.exit(0)