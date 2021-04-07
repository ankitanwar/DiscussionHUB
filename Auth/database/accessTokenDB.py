from pymongo import MongoClient

try:
    cluster=MongoClient(host="authdb",port=27017)
    db=cluster["User"]
    collection=db["AccessToken"]
except Exception as e:
    print("Error while connecting to the database{}".format(e))



class AccessToken:

    def SaveAccessToken(self,email,userID,accessToken,firstName):
        filter={"_id":userID}
        data={"email":email,"access_token":accessToken,"firstName":firstName}
        collection.update(filter,data,upsert=True)

    def GetAccessToken(self,userID):
        filter={"_id":int(userID)}
        result=collection.find_one(filter=filter)
        if result!=None:
            return result
    
    def delete_access_token(self,userID,accessToken):
        filter={"_id":int(userID),"access_token":accessToken}
        response=collection.find_one_and_delete(filter)
        return response
