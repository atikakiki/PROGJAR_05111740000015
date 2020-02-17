import sys
import socket

SIZE = 8 * 1024

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
    conn, client_address = sock.accept()
    print(f"connection from {client_address}")
    
    req = conn.recv(SIZE)
    client_req = open(req.decode(),"rb")
    print("Request Accepted")

    # Receive the data in small chunks and retransmit it   
    while True:
        recv_data=client_req.read(SIZE)
        if not recv_data : break
        conn.sendall(recv_data)
        print("Send data...")

    client_req.close()
    # Clean up the connection
    conn.close()
    print("-----Client Disconnected-----\n")
