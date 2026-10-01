import socket
import hashlib
import pyotp


# Part 2: Hash a password

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# Part 2: Verify a password

def verify_password(password, stored_hash):

    entered_hash = hash_password(password)

    return entered_hash == stored_hash


# Part 6: Verify a TOTP

def verify_otp(secret, otp):

    totp = pyotp.TOTP(secret)

    return totp.verify(otp)


# Part 7: Create Alice's TOTP secret

alice_secret = pyotp.random_base32()


# Part 7: Create the user database

users = {
    "alice": {
        "password_hash": hash_password(
            "mattias123!"
        ),
        "totp_secret": alice_secret
    }
}


# Part 10: Display Alice's secret for lab testing

print(
    "Alice's TOTP secret:",
    users["alice"]["totp_secret"]
)


# Part 10: Server settings

HOST = "127.0.0.1"
PORT = 12345


# Part 10: Create the TCP server socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server_socket.bind(
    (HOST, PORT)
)

server_socket.listen(1)

print(
    "Authentication server listening on",
    HOST,
    PORT
)


# Part 10: Accept one client

client_socket, client_address = server_socket.accept()

print(
    "Client connected:",
    client_address
)


# Part 10: Track authentication state

password_verified = False
current_user = None


# Part 10: Receive authentication messages

while True:

    data = client_socket.recv(1024)

    if not data:
        break

    message = data.decode().strip()

    print(
        "Received:",
        message
    )


    # Part 10A: Handle AUTH message

    if message.startswith("AUTH|"):

        parts = message.split("|")

        if len(parts) != 3:

            client_socket.sendall(
                b"ERROR|Invalid AUTH format"
            )

            continue


        username = parts[1]
        password = parts[2]


        # Check whether the username exists

        if username not in users:

            client_socket.sendall(
                b"ACCESS_DENIED"
            )

            continue


        # Verify the password

        stored_hash = users[username][
            "password_hash"
        ]

        if verify_password(
            password,
            stored_hash
        ):

            password_verified = True
            current_user = username

            client_socket.sendall(
                b"OTP_REQUIRED"
            )

        else:

            client_socket.sendall(
                b"ACCESS_DENIED"
            )


    # Part 10C: Handle OTP message

    elif message.startswith("OTP|"):

        parts = message.split("|")

        if len(parts) != 2:

            client_socket.sendall(
                b"ERROR|Invalid OTP format"
            )

            continue


        # OTP is only allowed after password verification

        if not password_verified:

            client_socket.sendall(
                b"ACCESS_DENIED"
            )

            continue


        otp = parts[1]

        secret = users[current_user][
            "totp_secret"
        ]


        if verify_otp(
            secret,
            otp
        ):

            client_socket.sendall(
                b"ACCESS_GRANTED"
            )

        else:

            client_socket.sendall(
                b"ACCESS_DENIED"
            )


    # Unknown protocol message

    else:

        client_socket.sendall(
            b"ERROR|Unknown command"
        )


# Part 10: Close sockets cleanly

client_socket.close()
server_socket.close()

print("Server closed.")