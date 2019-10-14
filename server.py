import socket
import sys
 
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Define host
host = '127.0.0.1'
 
# define the communication port
port = 12345
 
# Bind the socket to the port
sock.bind((host, port))


# Wait for a connection
print ('waiting for a connection')
# connection, client = sock.accept()
 
# Receive the data in small chunks and retransmit it
data1 = sock.recv(16)
data2 = sock.recv(16)


print ('number 1 received "%s"' % data1)
print ('number 2 received "%s"' % data2)
num1 = list(map(int, data1.split()))
num2 = list(map(int, data2.split()))

data3 = num1[0]*num2[0]
print (data3)
sock.close()