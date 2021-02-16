from flask_restful import Resource,reqparse
from flask import request
from user.user import ValidateUser,UserMarshal
from DataBase.sqlDataBase import UserDataBase
import bcrypt

salt=bcrypt.gensalt()

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
            receviedPassword=bytes(data["password"],encoding='utf-8')
            hashed = bcrypt.hashpw(receviedPassword,salt)
            data["password"]=hashed
            UserDataBase(**data).add()
            return {"message":"User Created Successfully"},200
        except Exception as e:
            return {"message":"Error while creating the user {}".format(e)},500
    
    def delete(self):
        data=User.parser.parse_args()
        try:
            UserDataBase(email=data["email"]).deleteUser()
            return {"message":"User has been deleted successfully"},200
        except Exception as e:
            return {"message":"Error occured while deleting the user {}".format(e)},500
    
    def patch(self):
        data=User.parser.parse_args()
        email=request.headers.get("email")
        user=UserDataBase(email=email).searchByEmail()
        if user==None:
            return {"message":"Invalid credentials"},400
        if data["firstname"]=="":
            data["firstname"]=user[1]
        if data["lastname"]=="":
            data["lastname"]=user[2]
        if data["email"]!="":
            search=UserDataBase(email=data["email"]).searchByEmail()
            if search:
                return {"message":"Email already exist in the database"}
        if data["email"]=="":
            data["email"]=user[3]
        if data["password"]=="":
            data["password"]=user[4]
        try:
            UserDataBase(**data).updateDetails(user[0])
            return {"message":"Porfile updated successfully"}
        except Exception as e:
            return {"Error occured while upating the details {}".format(e)}

    
class UserVerify(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("email",type=str,required=True,help="Email cannot be empty")
    parser.add_argument("password",type=str,required=True,help="Password cannot be empty")


    def post(self):
        data=UserVerify.parser.parse_args()
        search=UserDataBase(email=data['email']).searchByEmail()
        if search==None:
            return {"message":"Invalid Email Address"},400
        receviedPassword=bytes(data["password"],encoding='utf-8')
        storedPassword=bytes(search[4],encoding='utf-8')
        checkPassword=bcrypt.checkpw(receviedPassword,storedPassword)
        if checkPassword==False:
            return {"message":"Invalid Credentials"},400
        else:
            isPrivate=request.headers.get("x-private")
            if isPrivate=="True":
                response=UserMarshal().isPrivate(search)
                return response
            else:
                response=UserMarshal().isPublic(search)
                return response
            
