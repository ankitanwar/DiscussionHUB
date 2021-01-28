from flask_restful import Resource
from flask import request
from user.user import ValidateUser
from user.user import AccessToken
from DataBase.sqlDataBase import UserDataBase

class User(Resource):

    def post(self):
        data=request.get_json()
        err=ValidateUser(**data).Validate()
        if err!=None:
            return err,400
        try:
            UserDataBase.add(**data)
            return {"message":"User Created Successfully"},200
        except Exception as e:
            return {"message":"Some Error has been occur while creating the user {}".format(e)}

    def get(self):
        check=AccessToken.verify()
        if check==False:
            return {"message":"Invalid access token"}
        data=request.get_json()
        err=ValidateUser(**data).login()
        if err!=None:
            return err

    def patch(self):
        check=AccessToken.verify()
        if check==False:
            return {"message":"Invalid access token"}
        data=request.get_json()


class UserLogin(Resource):
    def Login(self):
        pass



class UserHistory(Resource):
    def get(self):  #To get the user history from monoDB DATABASE
        pass 
    def delete(self):  #TO delete the user history from mongoDB database
        pass