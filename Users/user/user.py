from DataBase.sqlDataBase import UserDataBase
from flask import request


class ValidateUser:
    def __init__(self,firstname="",lastname="",email="",password=""):
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
        srchMail=UserDataBase(email=self.Email).searchByEmail()
        if srchMail!=None:
            return {"message":"Given Email is already registered"}
        if len(self.PassWord)<5:
            return {"message":"Password length should be more than 5"}
    
    def login(self):
        if "@" not in self.Email:
            return {"message":"Enter the valid email address"}
        if len(self.PassWord)<5:
            return {"message":"Invalid password"}
    

class UserMarshal:
    def isPublic(self,result):
        values={}
        values["id"]=result[0]
        values["firstName"]=result[1]
        values["email"]=result[3]
        return values
    def isPrivate(self,result):
        values={}
        values["id"]=result[0]
        values["firstName"]=result[1]
        values["lastName"]=result[2]
        values["email"]=result[3]
        return  values

