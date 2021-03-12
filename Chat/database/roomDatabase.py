from pymongo import MongoClient
from domain.user import Room
try:
    cluster=MongoClient(host="localhost",port=27017)
    db=cluster["Chat"]
    collection=db["Rooms"]
except Exception as e:
    print("Error while connecting to the database {}".format(e))

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
        collection.update(filter,makeAdmin)
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