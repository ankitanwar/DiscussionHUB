from pymongo import MongoClient

try:
    cluster=MongoClient(host="localhost")
    db=cluster["User"]
    collection=db["AccessToken"]
except Exception as e:
    print ("Error while connecting to the database".format(e))



class AccessTokenDB:
    def __init__(self,email="",id=-1):
        self.email=email
        self.id=id
    def CreateAccessToken(self):

        data={"_id":self.id,"email":self.email}
        collection.insert_one(data)

        pass
    def verifyAccessToken(self):
        result=collection.find_one({"email":self.email})
        if result!=None:
            return result
