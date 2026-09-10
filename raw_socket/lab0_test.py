# Part 1 — Your First Python Program
import socket
print("Socket library loaded successfully")

print("My first Python security program")

course = "FSCT 8561"
port = 12345
print(course)
print(port)

message = "Hello"
data = message.encode()
print(message)
print(data)
print(data.decode())

# Part 2 — Understanding Sockets
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP socket created successfully")
my_socket.close()



# What do the options mean?
#- `socket.AF_INET` → IPv4
#- `socket.SOCK_STREAM` → TCP

# Reflection Question 1

#1. What is a socket?
# A socket is an endpoint where my program is using to send or receive data over a network where it is identified by the IP address and port number. 

#2. What does `AF_INET` mean?
# AF_INET is used to specify the address family for the socket, which in this case is IPv4. It tells us that the socket will use IPv4 addresses.

#3. What does `SOCK_STREAM` mean?
# SOCK_STREAM represents in this case the socket type, meaning this socket uses TCP 

