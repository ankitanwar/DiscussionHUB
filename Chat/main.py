from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO
from Resources.resources import RoomResources
from Resources.user import User
app=Flask(__name__)
api=Api(app)
api.add_resource(RoomResources,"/room")
api.add_resource(User,"/room/<string:roomID>")
socketio=SocketIO(app)
app.secret_key="Dont expose it"


if __name__=="__main__":
    try:
        socketio.run(app,port=8085)
    except Exception as e:
        print("Error while starting the server {}".format(e))