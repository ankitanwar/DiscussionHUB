from Resources.room import Room
from Resources.user import User
from flask_restful import Api

api=Api()
api.add_resource(Room,"/room")
api.add_resource(User,"/room/<string:roomID>")