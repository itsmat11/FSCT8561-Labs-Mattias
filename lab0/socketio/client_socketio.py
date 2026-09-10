import socketio 

# Create a Socket.IO client instance
sio = socketio.Client()

# Event handler: runs when the connection is established
@sio.event
def connect():
    print("connection established")

# Event handler: runs when the client disconnects
@sio.event
def disconnect():
    print("disconnected from server")

# Connect to the server running on localhost, port 8080
sio.connect("http://localhost:8080")

# Emit a "message" event with some data (this triggers print_message() on the server)
sio.emit("message", {"data": "my_data"})

# Keep the client running to listen for events (blocks until disconnected)
sio.wait()