from pymongo import MongoClient
from domain.user import Room
import time

retries=5
while retries>0:
    try:
        cluster=MongoClient(host="roomdb",port=27017)
        db=cluster["Chat"]
        collection=db["Rooms"]
        break
    except Exception as e:
        print("Error While connecting to the databse {}".format(e))
        retries-=1
        print("max retires left",retries)
        time.sleep(3)

def CreateRoom(roomName):
    data={"name":roomName,"members":[]}
    ans=collection.insert_one(data)
    return ans

def GetRoomMembers(roomID):
    filter={"_id":roomID}
    result=collection.find_one(filter=filter)
    return result

def AddMembers(userID,roomID,admin=False):
    filter={"_id":roomID}
    add={'$push':{"members":{"userID":userID,"admin":admin}}}
    err=collection.update(filter,add)
    if err!=None:
        return {"message":"Error While Adding the Memeber{}".format(err)}
    else:
        return {"message":"User Has Been Added To The Room Successfully"}

def RemoveMember(memberID,roomID):
    filter={"_id":roomID}
    remove={"$pull":{"members":{"userID":memberID}}}
    try:
        collection.update(filter,remove)
    except Exception as e:
        return {"message":"Error While Removing The member From The Room{}".format(e)}

def MakeAdmin(roomID,memberID):
    filter={"_id":roomID,"members.userID":memberID}
    makeAdmin={"$set":{"members.$.admin":True}}
    try:
        response=collection.update(filter,makeAdmin)
        return response
    except Exception as e:
        return {"message":"Error While Making The user Admin{}".format(e)}

def CheckInRoom(roomID,userID):
    filter={"_id":roomID,"members.userID":userID}
    ans=collection.count(filter)
    if ans==0:
        return False
    return True

def checkAdmin(roomID,userID):
    filter={"_id":roomID,"members":{"userID":userID,"admin":True}}
    result=collection.count(filter)
    if result==0:
        return False
    return True

def update_room_name(roomID,roomName):
    filter={"_id":roomID}
    update={"$set":{"name":roomName}}
    try:
        response=collection.find_one_and_update(filter,update)
        return response
    except:
        return {"message":"Error While Updating The Room Name"}




