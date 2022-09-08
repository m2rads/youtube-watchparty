import socketio
import eventlet
import random
from flask import jsonify

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, enviorn):
    # allow a client or reject it
    print(sid, "connected")


roomIdList = []


@sio.event
def disconnect(sid):
    print(sid, "disconnected")


@sio.event
def join_room(sid, data):
    print(sid, data, " : sid and data")
    roomId = int(data['roomId'])
    username = data['username']
    result = roomId in roomIdList
    if result:
        sio.enter_room(sid, roomId)
        sio.emit("join_status", {"status": 200}, to=sid)
        sio.emit('Id', {'roomId': roomId, 'username': username}, to=sid)
    else:
        sio.emit("join_status", {"status": 404}, to=sid)


@sio.event
def create_room(sid, data):
    print(sid, data, " : created data")
    roomId = random.randint(1000, 9999)
    username = data['username']
    roomIdList.append(roomId)
    sio.enter_room(sid, roomId)
    sio.emit('Id', {'roomId': roomId, 'username': username}, to=sid)


@sio.event
def on_youtube_change(sid, data):
    print(sid, data)
    roomId = data['roomId']
    timeline = data['timeline']
    sio.emit('youtube_change', {
             'timeline': timeline},  skip_sid=sid, to=roomId)


@sio.event
def on_player_state(sid, data):
    print(sid, data)
    roomId = data['roomId']
    playState = data['playState']
    sio.emit('player_state', {
             'playState': playState},  skip_sid=sid, to=roomId)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
