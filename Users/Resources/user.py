from flask_restful import Resource,reqparse
from cryptography.fernet import Fernet
from flask import request
from user.user import ValidateUser
from DataBase.sqlDataBase import UserDataBase

key=Fernet.generate_key()
f=Fernet(key)

class User(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("firstname",type=str)
    parser.add_argument("lastname",type=str)
    parser.add_argument("email",type=str)
    parser.add_argument("password",type=str)


    def post(self):
        data=User.parser.parse_args()
        err=ValidateUser(**data).Validate()
        if err!=None:
            return err,400
        try:
            receivedPassword=bytes(data["password"],encoding='utf8')
            hashed = f.encrypt(receivedPassword)
            data["password"]=hashed
            UserDataBase(**data).add()
            return {"message":"User Created Successfully"},200
        except Exception as e:
            return {"message":"Some Error has been occur while creating the user {}".format(e)},400
    

class UserLogin(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("email",type=str,required=True,help="Email cannot be empty")
    parser.add_argument("password",type=str,required=True,help="Password cannot be empty")


    def post(self):
        data=UserLogin.parser.parse_args()
        search=UserDataBase(email=data['email']).searchByEmail()
        if search==None:
            return {"message":"Invalid Email Address"},400
        receivedPassword=bytes(data["password"],encoding='utf8')
        storedPassword=bytes(search[4],encoding='utf8')
        stored=f.decrypt(storedPassword)
        print("The value od stored and received password is",storedPassword,receivedPassword)
        if stored==receivedPassword:
            return{"message":"You have been logged in successfully"},200
        else:
            return {"message":"Invalid credentials"},401


class UserHistory(Resource):
    def get(self):  #To get the user history from monoDB DATABASE
        pass 
    def delete(self):  #TO delete the user history from mongoDB database
        pass