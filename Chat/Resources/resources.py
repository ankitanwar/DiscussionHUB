from flask_restful import Resource,reqparse
from flask import request
from services.chatService import RoomServices

def getUserID():
    userID=request.headers.get("userID")
    return userID


class RoomResources(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("room_name",type=str)


    def post(self):
        data=RoomResources.parser.parse_args()
        name=data["room_name"]
        if name=="":
            return {"message":"Please Enter The Valid Group Name"}
        userID=getUserID()
        res=RoomServices().CreateNewRoom(userID=userID,RoomName=name)
        return res