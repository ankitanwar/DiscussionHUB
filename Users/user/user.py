from flask_restful import Resource,reqparse
from DataBase.db import UserDataBase

class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('firstname',type=str,required=True,help="First Name cannot be empty")
    parser.add_argument('lastname',type=str)
    parser.add_argument('email',type=str,required=True,help="Email cannot be empty")
    parser.add_argument('password',type=str,required=True,help="Password cannot be empty")

    def post(self):
        data=User.parser.parse_args()
        err=ValidateUser(**data).Validate()
        if err!=None:
            return err,400
        UserDataBase.add(*data)
        return {"message":"User Created Successfully"},200

    def get(self):
        data=User.parser.parse_args()
        err=ValidateUser(**data).login()
        if err!=None:
            return err
        

class ValidateUser:
    def __init__(self,firstname,lastname,email,password):
        self.FirstName=firstname
        self.lastname=lastname
        self.Email=email
        self.PassWord=password

    def Validate(self):
        if self.FirstName=="":
            return {"message":"First name cannot be empty"}
        if self.Email=="":
            return {"message":"Email cannot be empty"}
        if "@" not in self.Email:
            return {"message":"Please enter the valid email address"}
        srchMail=UserDataBase.searchByEmail(self.Email)
        if srchMail!=None:
            return {"message":"Given Email is already registered"}
        if len(self.PassWord)<5:
            return {"message":"Password length should be more than 5"}
    
    def login(self):
        if "@" not in self.Email:
            return {"message":"Enter the valid email address"}
        if len(self.PassWord)<5:
            return {"message":"Invalid password"}

