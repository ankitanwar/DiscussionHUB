from pymongo import MongoClient

try:
    cluster=MongoClient(host="127.0.0.1",port=27017)
    db=cluster["User"]
    collection=db["AccessToken"]
except Exception as e:
    print("Error while connecting to the database{}".format(e))



class AccessToken:
    def SaveAccessToken(self,email,userID,accessToken,firstName):
        filter={"_id":userID}
        data={"email":email,"userID":userID,"access_token":accessToken,"firstName":firstName}
        result=collection.update(filter,data,upsert=True)
        print("The value of rsult in accessTokenDb is",result)

    def GetAccessToken(self,userID):
        filter={"_id":userID}
        result=collection.find_one(filter)
        if result!=None:
            return result
