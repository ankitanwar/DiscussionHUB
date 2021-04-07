from flask_restful import Resource,reqparse
from flask import request,jsonify
from user.user import ValidateUser
from services.services import UserService
import requests
from functools import wraps



def autheticateUser(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        url="http://auth:8082/access"
        req=requests.get(url,headers=request.headers)
        response=req.json()
        if response["message"]!="valid":
            return jsonify({"message":"Invalid Token ID"})
        return f(*args,**kwargs)
    return decorated

class User(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("firstname",type=str)
    parser.add_argument("lastname",type=str)
    parser.add_argument("email",type=str)
    parser.add_argument("password",type=str)


    def post(self):
        data=User.parser.parse_args()
        checkDetails=ValidateUser(**data).Validate()
        if checkDetails!=None:
            return checkDetails,400
        firstName=data["firstname"]
        lastName=data["lastname"]
        email=data["email"]
        password=data["password"]
        response=UserService().createNewUser(firstName,lastName,email,password)
        return response

    @autheticateUser
    def delete(self):
        userID=request.headers.get("X-Caller-ID")
        response=UserService().deleteUserAccount(userID)
        return response

        
    @autheticateUser
    def patch(self):
        data=User.parser.parse_args()
        userID=request.headers.get("X-Caller-ID")
        firstName=data["firstname"]
        lastname=data["lastname"]
        email=data["email"]
        response=UserService().ModifyDetails(userID=userID,email=email,firstName=firstName,lastName=lastname)
        return response

    @autheticateUser
    def get(self):
        userID=request.headers.get("X-Caller-ID")
        details=UserService().getUserDetails(userID)
        return details
        

    
class UserVerify(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("email",type=str,required=True,help="Email cannot be empty")
    parser.add_argument("password",type=str,required=True,help="Password cannot be empty")

    def post(self):
        data=UserVerify.parser.parse_args()
        email=data["email"]
        password=data["password"]
        response=UserService().verifyUser(email,password)
        return response
    
    @autheticateUser
    def patch(self):
        userID=request.headers.get("X-USER-ID")
        data=UserVerify().parser.parse_args()
        password=data["password"]
        response=UserService().changePassword(userID,password)
        return response
