from DataBase.sqlDataBase import UserDataBase
from flask import jsonify,request
from user.user import UserMarshal
import bcrypt

salt=bcrypt.gensalt()

class UserService:
    def deleteUserAccount(self,email):
        if not email:
            return jsonify({"message":"Invalid Email Address"})
        UserDataBase(email=email).deleteUser()
        return {"message":"User has been deleted successfully"},200

    def getUserDetails(self,userID):
        result=UserDataBase().searchByID(id=userID)
        isPrivate=request.headers.get("x-private")
        if isPrivate=="True":
            response=UserMarshal().isPrivate(result)
            return response
        else:
            response=UserMarshal().isPublic(result)
            return response 

    def ModifyDetails(self,userID,email="",firstName="",lastName=""):
        savedInfo=UserDataBase().searchByID(id=userID)
        if not email:
            email=savedInfo[3]
        if not firstName:
            firstName=savedInfo[1]
        if not lastName:
            lastName=savedInfo[2]
        UserDataBase(firstName,lastName,email).updateDetails(id=userID)
        return jsonify({"message":"User Details Has Been Updated Successfully"})

    def changePassword(self,userID,password):
        receviedPassword=bytes(password,encoding='utf-8')
        hashed = bcrypt.hashpw(receviedPassword,salt)
        password=hashed
        UserDataBase(password=password).updatePassword(userID)
        return jsonify({"message":"Password Has Been Updated Successfully"})


    def createNewUser(self,firstName="",lastName="",email="",password=""):
        receviedPassword=bytes(password,encoding='utf-8')
        hashed = bcrypt.hashpw(receviedPassword,salt)
        password=hashed
        UserDataBase(firstName,lastName,email,password).add()
        return jsonify({"message":"User Created Successfully"})

    def verifyUser(self,email,password):
        if not email:
            return jsonify({"message":"Please Enter The valid Email Address"})
        if not password or len(password)<5:
            return jsonify({"message":"Invalid credentials"})
        searchUser=UserDataBase(email=email).searchByEmail()
        receviedPassword=bytes(password,encoding='utf-8')
        storedPassword=bytes(searchUser[4],encoding='utf-8')
        checkPassword=bcrypt.checkpw(receviedPassword,storedPassword)
        if checkPassword==False:
            return {"message":"Invalid Credentials"},400
        else:
            isPrivate=request.headers.get("x-private")
            if isPrivate=="True":
                response=UserMarshal().isPrivate(searchUser)
                return response
            else:
                response=UserMarshal().isPublic(searchUser)
                return response



