from flask_restful import Resource
from flask import request
from user.user import ValidateUser
from DataBase.sqlDataBase import UserDataBase

class User(Resource):

    def post(self):
        data=request.get_json()
        err=ValidateUser(**data).Validate()
        if err!=None:
            return err,400
        try:
            userRequest=UserDataBase(**data).add()
            print("The values are",userRequest.lastname,userRequest.firstname,userRequest.email)
            return {"message":"User Created Successfully"},200
        except Exception as e:
            return {"message":"Some Error has been occur while creating the user {}".format(e)},400
    

class UserLogin(Resource):
    def get(self):
        data=request.get_json()
        search=UserDataBase(email=data['email'])
        if search==None:
            return {"message":"Invalid Email Address"},400
        



class UserHistory(Resource):
    def get(self):  #To get the user history from monoDB DATABASE
        pass 
    def delete(self):  #TO delete the user history from mongoDB database
        pass