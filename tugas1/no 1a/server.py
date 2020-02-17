import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # get filename of recived file
    file_recv = open("receive.txt","wb")
    print("\nCopied file's filename is receive.txt\n")
   
    # Receive the data 
    while True:
        RecvData = connection.recv(1024)
        if not RecvData:
            break
        file_recv.write(RecvData)
    file_recv.close()
    print('File received')
    # Clean up the connection
    connection.close()
    print("-----Client disconnected-----\n")
  