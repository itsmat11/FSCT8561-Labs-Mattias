import socket
from getpass import getpass


# Part 11: Server settings

HOST = "127.0.0.1"
PORT = 12345


# Part 11: Create the client socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


# Part 11: Connect to the authentication server

client_socket.connect(
    (HOST, PORT)
)


# Part 11: Ask for username and password

username = input("Username: ")
password = getpass("Password: ")


# Part 11: Send AUTH message

auth_message = (
    "AUTH|"
    + username
    + "|"
    + password
)

client_socket.sendall(
    auth_message.encode()
)


# Part 11: Wait for server response

response = client_socket.recv(
    1024
).decode()

print("Server:", response)


# Part 11: Only ask for OTP if password was accepted

if response == "OTP_REQUIRED":

    otp = input("OTP: ")

    otp_message = (
        "OTP|"
        + otp
    )

    client_socket.sendall(
        otp_message.encode()
    )


    # Part 11: Receive final authentication result

    final_response = client_socket.recv(
        1024
    ).decode()

    print("Server:", final_response)


# Part 11: Close the connection cleanly

client_socket.close()