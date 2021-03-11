import database.db as db
from flask import jsonify

class FeedService:
    def addNewContent(self,userName,userID,Content):
        response=db.PostContent(userID,userName,Content)
        if response!=None:
            return {"message":"Error While Posting The Content"}
        else:
            return{"message":"Content Has Been Posted Successfully"}
    def deleteContent(self):
        pass
    def modifyContent(self):
        pass
    def ViewAllContentOfParticularUser(self,userID):
        response=db.ViewContent(userID)
        if response==None:
            return {"message":"No Data Found"}
        else:
            return jsonify(response["Content"])


class jobPost:
    def __init__(self,skils,experience,role,linkForRegistration):
        self.skils=skils
        self.experience=experience
        self.role=role
        self.linkForRegistration=linkForRegistration

    def PostNewJob(self):
        return self
