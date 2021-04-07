from pymongo import MongoClient
from domain.domain import FeedDomain
import time

retries=5
while retries>0:
    try:
        cluster=MongoClient(host="feeddb",port=27017)
        db=cluster["DiscussionHUB"]
        collection=db["feeds"]
        userCollection=db["users"]
        break
    except Exception as e:
        print("Error While connecting to the databse {}".format(e))
        retries-=1
        print("max retires left",retries)
        time.sleep(3)


class Feeds:
    
    def addPost(self,FeedDomain):
        details={"userID":FeedDomain.userID,"userName":FeedDomain.userName,"company":FeedDomain.company,"role":FeedDomain.role,"description":FeedDomain.description,"experience":FeedDomain.experience}
        response=collection.insert_one(details)
        return response


    def getPost(self,postID):
        filter={"_id":postID}
        result=collection.find_one(filter)
        return result

    def ModifyPost(self,postID,FeedDomain):
        filter={"_id":postID}
        update={"$set":{"company":FeedDomain.company,"description":FeedDomain.description,"role":FeedDomain.role,"experience":FeedDomain.experience}}
        response=collection.find_one_and_update(filter,update,upsert=False)
        return response
    
    def deletePost(self,userID,postID):
        filter={"_id":postID,"userID":userID}
        response=collection.find_one_and_delete(filter,upsert=False)
        return response
    
    def filterByExperience(self,experience):
        filter={"experience":experience}
        result=collection.find(filter)
        return result
    
    def filterByRole(self,role):
        filter={"role":role}
        result=collection.find(filter)
        return result
    
    def filterByCompany(self,companyName):
        filter={"company":companyName}
        result=collection.find(filter)
        return result


class UserFeed:

    def addNewPost(self,FeedDomain,postID):
        filter={"_id":FeedDomain.userID}
        add={'$push':{"Content":{"company":FeedDomain.company,"role":FeedDomain.role,"description":FeedDomain.description,"experience":FeedDomain.experience,"postID":postID}}}
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
    
    def ModifyPost(self,postID,FeedDomain):
        filter={"_id":FeedDomain.userID,"Content.postID":postID}
        update={"$set":{"Content":{"company":FeedDomain.company,"description":FeedDomain.description,"role":FeedDomain.role,"experience":FeedDomain.experience,"postID":postID}}}
        userCollection.update_one(filter,update)
