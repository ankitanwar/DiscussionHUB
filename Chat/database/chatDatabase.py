from pymongo import MongoClient
from domain.user import Room
import time

retries=5
while retries>0:
    try:
        cluster=MongoClient(host="chatdb",port=27017)
        db=cluster["Chat"]
        collection=db["messages"]
        break
    except Exception as e:
        print("Error While connecting to the databse {}".format(e))
        retries-=1
        print("max retires left",retries)
        time.sleep(3)

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

