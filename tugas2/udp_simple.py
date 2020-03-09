
import socket

TARGET_IP = "10.151.254.249"
TARGET_PORT = 5006

nama='Hallo Chaniyah (05111740000115), ini Kiki (05111740000015)'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(nama.encode()),(TARGET_IP,TARGET_PORT))