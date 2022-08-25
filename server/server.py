from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit


app = Flask(__name__)
socket = SocketIO(app)


@socket.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)


@socket.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


if __name__ == '__main__':
    socket.run(app)
