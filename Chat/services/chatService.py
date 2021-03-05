from domain.user import User,Room
import database.chatDatabase as db
from bson import ObjectId


class RoomServices:
    def CreateNewRoom(self,userID,RoomName):
        if len(RoomName)<=0:
            return {"message":"Please Enter The valid Room Name"},400
        try:
            res=db.CreateRoom(RoomName)
            roomID=res.inserted_id
            print("The value of room ID is",roomID)
        except Exception as e:
            return {"message":"Error While Creating the Room {}".format(e)}
        try:
            db.AddMembers(userID,roomID,admin=True)
        except Exception as e:
            return {"message":"Error While Creating the Room {}".format(e)}
        

    def GetRoomMembers(self,roomID,userID):
        if len(roomID)<=0:
            return {"message":"Invalid Room Address"},404

    def UpdateRoom(self,roomID,details):
        pass


    def AddMemberInRoom(self,adminID,memberID,roomID):
        print("Resoucres is working fine")
        if len(memberID)==0:
            return {"message":"Invalid User"}
        try:
            roomID=ObjectId(roomID)
            db.AddMembers(memberID,roomID)
            return {"message":"User Has Been Added Successfully"}
        except Exception as e:
            return {"message":"Error While Adding The Memeber Into The Room {}".format(e)}

    def RemoveMember(self,adminID,userID,roomID):
        roomID=ObjectId(roomID)
        try:
            db.RemoveMember(memberID=userID,roomID=roomID)
            return {"message":"Member Has Been Removed Successfully"}
        except Exception as e:
            return {"message":"Error While Removing The Member {}".format(e)}

    def MakeAdmin(self,adminID,memberID,roomID):
        roomID=ObjectId(roomID)
        try:
            db.MakeAdmin(roomID,memberID)
            return {"message":"User Has Been Addedd To The Admin Successfully"}
        except Exception as e:
            return("Error While Making The Member Admin{}".format(e))
    
    def IsRoomMember(self,roomID,memberID):
        roomID=ObjectId(roomID)
        check=db.CheckInRoom(roomID=roomID,userID=memberID)
        if check==None:
            return {"message":"No User Exist"},404
        print(check)

def SaveMessage(message,userID):
    pass



    
    
    

