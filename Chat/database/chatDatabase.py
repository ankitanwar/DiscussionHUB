from pymongo import MongoClient
from domain.user import Room
try:
    cluster=MongoClient(host="localhost",port=27017)
    db=cluster["Chat"]
    collection=db["messages"]
except Exception as e:
    print("Error while connecting to the database {}".format(e))

class chatDB:

    def saveMessage(self,roomID,message):
        filter={"_id":roomID}
        saveMessage={'$push':{"messages":message}}
        collection.update_one(filter,saveMessage,upsert=True)
    
    def fetchOlderMessages(self,roomID):
        filter={"_id":roomID}
        limit={"messages":{"$slice": -10}}
        messages=collection.find(filter,limit)
        return messages

