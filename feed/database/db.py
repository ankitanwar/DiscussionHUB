from pymongo import MongoClient

try:
    cluster=MongoClient(host="localhost",port=27017)
    db=cluster["feeds"]
    collection=db["feeds"]
    userCollection=db["users"]
except Exception as e:
    print("Error While connecting to the databse {}".format(e))


class Feeds:
    
    def addPost(self,content):
        response=collection.insert_one(content)
        return response


    def getPost(self,postID):
        filter={"_id":postID}
        result=collection.find_one(filter)
        return result

    def ModifyPost(self):
        pass
    
    def deletePost(self,userID,postID):
        filter={"_id":postID,"userID":userID}
        ans=collection.delete_one(filter)
        print("The value of ans is",ans)
    
    def filterValues(self,experience,role,company):
        filter={"experience":experience,"role":role,"company":company}
        result=collection.find(filter)
        return result


class UserFeed:

    def addNewPost(self,userID,userName,content):
        filter={"_id":userID}
        add={'$push':{"Content":content}}
        response=userCollection.update(filter,add,upsert=True)
        return response

    def ViewAllContent(self,userID):
        filter={"_id":userID}
        result=userCollection.find_one(filter)
        return result

    def deleteContent(self,userID,postID):
        filter={"_id":userID}
        remove={"$pull":{"Content":{"postID":postID}}}
        userCollection.update_one(filter,remove)
