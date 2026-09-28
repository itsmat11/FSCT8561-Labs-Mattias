import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("Client connected:", sid)


@sio.event
def disconnect(sid):
    print("Client disconnected:", sid)


@sio.event
def message(sid, data):
    print("Received:", data)

    sio.emit(
        "response",
        "Message received: " + data,
        to=sid
    )


if __name__ == "__main__":
    import eventlet

    eventlet.wsgi.server(
        eventlet.listen(("127.0.0.1", 12345)),
        app
    )
