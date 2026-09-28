import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("Connected to server")


@sio.event
def disconnect():
    print("Disconnected from server")


@sio.on("response")
def response(data):
    print("Server:", data)


sio.connect("http://127.0.0.1:12345")

username = input("Enter your username: ")

sio.send("HELLO|" + username)

while True:

    message = input(
        "Enter message or type EXIT to leave: "
    )

    if message.upper() == "EXIT":
        sio.send("EXIT|")
        break

    sio.send("MSG|" + message)

sio.disconnect()
