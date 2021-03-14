import database.db as db
from flask import jsonify
from bson.objectid import ObjectId

class FeedService:
    def addNewContent(self,userID,userName,Content):
        try:
            Content["userID"]=userID
            db.Feeds().addPost(Content)
            Content.pop("userID")
        except:
            return {"message":"Error while Adding the post"}
        
        try:
            db.UserFeed().addNewPost(userID,userName,Content)
            return {"message":"Successfully Added The post"}
        except:
            return {"message":"Error While Adding The Post"},500

    def deleteContent(self,userID,postID):
        postID=ObjectId(postID)
        try:
            db.Feeds().deletePost(userID,postID)
            db.UserFeed().deleteContent(userID,postID)
            return {"message":"Post Has Been Deleted Successfully"},200
        except:
            return {"message":"Error while deleting the post"},500

    def modifyContent(self,userID,postID):
        pass

    def ViewContentOfUser(self,userID):
        try:
            response=db.UserFeed().ViewAllContent(userID)
        except:
            return {"message":"Unable To Fetch The Posts...."},500
        if response==None:
            return {"message":"No Data Found"}, 404
        else:
            for values in response["Content"]:
                values["_id"]=str(values["_id"])
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