from flask_restful import Resource,reqparse
from services.chatService import RoomServices
from Resources.resources import getUserID
class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("memberID")

    def post(self,roomID):
        data=User.parser.parse_args()
        userID=getUserID()
        result=RoomServices().AddMemberInRoom(adminID=userID,memberID=data["memberID"],roomID=roomID)
        return result

    def delete(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        result=RoomServices().RemoveMember(adminID=adminID,userID=data["memberID"],roomID=roomID)
        return result

    def put(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        result=RoomServices().MakeAdmin(adminID=adminID,memberID=data["memberID"],roomID=roomID)
        return result
    
    def get(self,roomID):
        userID=getUserID()
        RoomServices().IsRoomMember(roomID=roomID,memberID=userID)