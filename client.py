import socket
import sys
 
# Create a UDP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Define host
host = '127.0.0.1'
 
# define the communication port
port = 12345
 
# Connect the socket to the port where the server is listening
server_address = ((host, port))
print ("connecting")
stream_socket.connect(server_address)
 
# Send data

message1 = input("number 1 : ")
message2 = input('number 2 : ')

if message1 and message2:
    stream_socket.sendall(message1.encode())
    stream_socket.sendall(message2.encode())

else:
    print('input number is null')
    stream_socket.close()