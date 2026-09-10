from aiohttp import web
import socketio 

# Create an async Socket.IO server instance
socket_io = socketio.AsyncServer()

# Create the web application and attach Socket.IO to it
app = web.Application()
socket_io.attach(app)

# Basic HTTP route for the root URL
async def index(request):
    return web.Response(text="Hello world from socketio", content_type="text/html")

# Event handler: runs whenever a client emits a "message" event
@socket_io.on("message")
def print_message(socket_id, data):
    print("Socket ID:", socket_id)
    print("Data:", data)

# Register the index route
app.router.add_get("/", index)

# Start the server (runs on http://localhost:8080 by default)
if __name__ == "__main__":
    web.run_app(app)