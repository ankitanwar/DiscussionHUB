import database.db as db
from flask import jsonify
from bson.objectid import ObjectId
from domain.domain import FeedDomain

class FeedService:
    def addNewContent(self,FeedDomain):
        try:
            response=db.Feeds().addPost(FeedDomain)
        except Exception as e:
            print("the value of error is",e)
            return {"message":"Error while Adding the post"}
        
        try:
            postID=str(response.inserted_id)
            db.UserFeed().addNewPost(FeedDomain,postID)
            return {"message":"Successfully Added The post"}
        except Exception as e:
            db.Feeds().deletePost(FeedDomain.userID,response.inserted_id)
            return {"message":"Error While Adding The Post2"},500

    def deleteContent(self,userID,postID):
        postIDKey=ObjectId(postID)
        try:
            response=db.Feeds().deletePost(userID,postIDKey)
            if response==None:
                return {"message":"Unable To Delete The post"},500
            db.UserFeed().deleteContent(userID,postID)
            return {"message":"Post Has Been Deleted Successfully"},200
        except Exception as e:
            print("The value of error is",e)
            return {"message":"Error while deleting the post"},500

    def modifyContent(self,userID,postID,FeedDomain):
        postIDKey=ObjectId(postID)
        savedDetaills=db.Feeds().getPost(postIDKey)
        if savedDetaills==None:
            return {"message":"Unable To Fetch The Details"},404
        if FeedDomain.company=="":
            FeedDomain.company=savedDetaills["company"]
        if FeedDomain.description=="":
            FeedDomain.description=savedDetaills["description"]
        if FeedDomain.experience=="":
            FeedDomain.experience=savedDetaills['experience']
        if FeedDomain.role=="":
            FeedDomain.role=savedDetaills["role"]
        try:
            response=db.Feeds().ModifyPost(postIDKey,FeedDomain)
            if response==None:
                return{"message":"Unable To Update The post"},500
            db.UserFeed().ModifyPost(postID,FeedDomain)
            return {"message":"Post Has Been Updated Successfully"},200
        except:
            return {"message":"Error While Updating The Details"},500


    def ViewContentOfUser(self,userID):
        try:
            response=db.UserFeed().ViewAllContent(userID)
        except:
            return {"message":"Unable To Fetch The Posts...."},500
        if response==None:
            return {"message":"No Data Found"}, 404
        else:
            for values in response["Content"]:
                values["postID"]=str(values["postID"])
            return response["Content"]
        
    def getPost(self,postID):
        postID=ObjectId(postID)
        try:
            response=db.Feeds().getPost(postID)
            if response==None:
                return {"message":"No Post Found"},404
            else:
                response["_id"]=str(response["_id"])
                return response
        except:
            return {"message":"Couldn't Fetch The post...Please Try again"},500
    
    def filterPost(self,experience,role,company):
        try:
            result=db.Feeds().filterValues(experience,role,company)
            return result
        except:
            return {"message":"Cannot Filter Values According to the result"}