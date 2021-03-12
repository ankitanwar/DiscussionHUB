from domain.user import User,Room
import database.roomDatabase as roomdb
from bson import ObjectId
from flask_socketio import join_room,leave_room,send
from sockets import socketio

class RoomServices:
    def CreateNewRoom(self,userID,RoomName):
        if len(RoomName)<=0:
            return {"message":"Please Enter The valid Room Name"},400
        try:
            res=roomdb.CreateRoom(RoomName)
            roomID=res.inserted_id
        except Exception as e:
            return {"message":"Error While Creating the Room {}".format(e)}
        try:
            roomdb.AddMembers(userID,roomID,admin=True)
        except Exception as e:
            return {"message":"Error While Creating the Room {}".format(e)}     

    def GetRoomMembers(self,roomID,userID):
        if len(roomID)<=0:
            return {"message":"Invalid Room Address"},404
        roomID=ObjectId(roomID)
        result=roomdb.GetRoomMembers(roomID)
        return result["members"]

    def UpdateRoom(self,roomID,details):
        pass

    @socketio.on("join_room")
    def AddMemberInRoom(self,memberID,roomID):
        if len(memberID)==0:
            return {"message":"Invalid User"}
        try:
            roomID=ObjectId(roomID)
            roomdb.AddMembers(memberID,roomID)
            return {"message":"User Has Been Added Successfully"}
        except Exception as e:
            return {"message":"Error While Adding The Memeber Into The Room {}".format(e)}
        send("member " + memberID + "has joined the room")

    @socketio.on("leave_room")
    def RemoveMember(self,userID,roomID):
        roomID=ObjectId(roomID)
        try:
            roomdb.RemoveMember(memberID=userID,roomID=roomID)
            send("member"+userID+"has been removed from the room")
            return {"message":"Member Has Been Removed Successfully"}
        except Exception as e:
            return {"message":"Error While Removing The Member {}".format(e)}

    def MakeAdmin(self,memberID,roomID):
        roomID=ObjectId(roomID)
        try:
            roomdb.MakeAdmin(roomID,memberID)
            return {"message":"User Has Been Addedd To The Admin Successfully"}
        except Exception as e:
            return("Error While Making The Member Admin{}".format(e))
    
    def IsRoomMember(self,roomID,memberID):
        if not roomID:
            return False
        if not memberID:
            return False
        roomID=ObjectId(roomID)
        check=roomdb.CheckInRoom(roomID=roomID,userID=memberID)
        return check
    
    def checkAdmin(self,roomID,adminID):
        if not roomID:
            return False
        if not adminID:
            return False
        roomID=ObjectId(roomID)
        response=roomdb.checkAdmin(roomID,adminID)
        return response

    
    
    

