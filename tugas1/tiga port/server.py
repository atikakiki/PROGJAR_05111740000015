import sys
import socket
import threading

def port_thread(i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('127.0.0.1', i)
    print(f"starting up on {server_address}")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        print(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print(f"received {data}")
            if data:
                print("sending back data")
                connection.sendall(data)
            else:
                break
            
        # Clean up the connection
        connection.close()

if __name__ == "__main__":

    threads=[]
    t1 = threading.Thread(target=port_thread, args=(31000,))
    threads.append(t1)
    t2 = threading.Thread(target=port_thread, args=(31001,))
    threads.append(t2)
    t3 = threading.Thread(target=port_thread, args=(31002,))
    threads.append(t3)

    for i in threads:
        i.start()