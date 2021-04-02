from flask_restful import Resource,reqparse
from services.roomsService import RoomServices
from Resources.room import getUserID


class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("memberID")

    def post(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Add Member Into The Room"}, 400
        checkAlreadyInRoom=RoomServices().IsRoomMember(roomID,data["memberID"])
        if checkAlreadyInRoom==True:
            return {"message":"User Is Already In The Room"}, 400
        result=RoomServices().AddMemberInRoom(memberID=data["memberID"],roomID=roomID)
        return result

    def delete(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Remove Member From The Group"}, 400
        result=RoomServices().RemoveMember(userID=data["memberID"],roomID=roomID)
        return result

    def put(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Delete Member From The Group"}, 400
        result=RoomServices().MakeAdmin(memberID=data["memberID"],roomID=roomID)
        return result
    
    def get(self,roomID):
        userID=getUserID()
        check=RoomServices().IsRoomMember(roomID=roomID,memberID=userID)
        if check!=True:
            return {"message":"No Room Exist With Given ID"},404
        response=RoomServices().GetRoomMembers(roomID=roomID,userID=userID)
        return response