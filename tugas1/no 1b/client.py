import sys
import socket

SIZE = 8 * 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    message = 'file_request.txt'
    print(f"sending {message} as request")
    sock.sendall(message.encode())
    
    # Look for the response
    result_req = open("request_result.txt","wb")
    if not result_req:
        print("Data Rejected\n")
    result_req.write(sock.recv(SIZE))
    print("Data Accepted\n")
    
finally:
    sock.close()
    print("Request Finish")
