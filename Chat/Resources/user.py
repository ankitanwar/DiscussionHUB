from flask_restful import Resource,reqparse
from services.roomsService import RoomServices
from Resources.room import getUserID,authenticate_request
from flask import request
import requests


class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("memberID")

    @authenticate_request
    def post(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        checkAlreadyInRoom=RoomServices().IsRoomMember(roomID,data["memberID"])
        if checkAlreadyInRoom==True:
            return {"message":"User Is Already In The Room"}, 400
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Add Member Into The Room...Only Admins Are Allowed To Do So"}, 400
        result=RoomServices().AddMemberInRoom(memberID=data["memberID"],roomID=roomID)
        return result


    @authenticate_request
    def delete(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Remove Member From The Group...Only Admin Can Remove The Members"}, 400
        result=RoomServices().RemoveMember(userID=data["memberID"],roomID=roomID)
        return result


    @authenticate_request
    def put(self,roomID):
        data=User.parser.parse_args()
        adminID=getUserID()
        check=RoomServices().checkAdmin(roomID,adminID)
        if check!=True:
            return {"message":"Cannot Delete Member From The Group....Only Admin Has The Power"}, 400
        result=RoomServices().MakeAdmin(memberID=data["memberID"],roomID=roomID)
        return result
    

    @authenticate_request
    def get(self,roomID):
        userID=getUserID()
        check=RoomServices().IsRoomMember(roomID=roomID,memberID=userID)
        if check!=True:
            return {"message":"No Room Exist With Given ID"},404
        response=RoomServices().GetRoomMembers(roomID=roomID,userID=userID)
        return response
    
    @authenticate_request
    def patch(self,roomID):
        adminID=getUserID()
        check_admin=RoomServices().checkAdmin(roomID,adminID)
        if check_admin==False:
            return {"message":"Only Admin Can Update The Room Name....."}
        req=request.get_json()
        newRoomName=req["room_name"]
        response=RoomServices().UpdateRoom(roomID,newRoomName)
        return response