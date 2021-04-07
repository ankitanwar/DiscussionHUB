from flask_restful import Resource,reqparse
from flask import request,jsonify
from services.roomsService import RoomServices
import requests
from functools import wraps

def getUserID():
    userID=request.headers.get("X-Caller-ID")
    return userID

def authenticate_request(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        url="http://127.0.0.1:8082/access"
        req=requests.get(url,headers=request.headers)
        response=req.json()
        if response["message"]!="valid":
            return jsonify({"message":"Invalid Token ID"})
        return f(*args,**kwargs)
    return decorated

class Room(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("room_name",type=str)

    @authenticate_request
    def post(self):
        data=Room.parser.parse_args()
        name=data["room_name"]
        if name=="":
            return {"message":"Please Enter The Valid Group Name"}
        userID=getUserID()
        res=RoomServices().CreateNewRoom(userID=userID,RoomName=name)
        return res
