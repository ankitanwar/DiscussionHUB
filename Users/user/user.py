from DataBase.sqlDataBase import UserDataBase
from flask import request
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
        srchMail=UserDataBase().searchByEmail(self.Email)
        if srchMail!=None:
            return {"message":"Given Email is already registered"}
        if len(self.PassWord)<5:
            return {"message":"Password length should be more than 5"}
    
    def login(self):
        if "@" not in self.Email:
            return {"message":"Enter the valid email address"}
        if len(self.PassWord)<5:
            return {"message":"Invalid password"}

class AccessToken:

    def create(): #create only 1 access token for a user
        pass
    
    def verify():
        token=request.headers.get("access_token")
        return False #return false if accesstoken is invalid else true
