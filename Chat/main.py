from flask import Flask
from endpoints import api
from sockets import socketio


app=Flask(__name__)
api.init_app(app)
socketio.init_app(app)

if __name__=="__main__":
    try:
        socketio.run(app,host="0.0.0.0",port=8085,debug=True)
    except Exception as e:
        print("Error while starting the server {}".format(e))