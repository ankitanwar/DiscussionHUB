from DataBase.sqlDataBase import UserDataBase
from flask import jsonify,request
from user.user import UserMarshal
import bcrypt

salt=bcrypt.gensalt()

class UserService:
    def deleteUserAccount(self,userID):
        if not userID:
            return jsonify({"message":"Invalid Email Address"})
        try:
            UserDataBase().deleteUser(userID=userID)
            return {"message":"User has been deleted successfully"},200
        except:
            return {"message":"Some Error Has Been Occured While Deleting The Account"}, 500

    def getUserDetails(self,userID):
        try:
            result=UserDataBase().searchByID(id=userID)
            if result==None:
                return {"message":"Unable To Fetch The User Details"},404
        except:
            return {"message":"Some Internal Error Has Been Occured While Fetch The Details"},500
        
        isPrivate=request.headers.get("x-private")
        if isPrivate=="True":
            response=UserMarshal().isPrivate(result)
            return response
        else:
            response=UserMarshal().isPublic(result)
            return response 

    def ModifyDetails(self,userID,email="",firstName="",lastName=""):
        try:
            savedInfo=UserDataBase().searchByID(id=userID)
            if savedInfo==None:
                return {"message":"Unable To Fetch The User Details"}
        except:
            return {"message":"Some Internal Error Has Been Occured While Fetch The Details"},500
        if savedInfo==None:
            return {"message":"Unable To Fetch The User Details"},404
        if not email:
            email=savedInfo[3]
        if not firstName:
            firstName=savedInfo[1]
        if not lastName:
            lastName=savedInfo[2]
        try:
            UserDataBase(firstName,lastName,email).updateDetails(id=userID)
            return jsonify({"message":"User Details Has Been Updated Successfully"})
        except:
            return {"message":"Error While Updating The Details"},500

    def changePassword(self,userID,password):
        receviedPassword=bytes(password,encoding='utf-8')
        hashed = bcrypt.hashpw(receviedPassword,salt)
        password=hashed
        try:
            UserDataBase(password=password).updatePassword(userID)
            return jsonify({"message":"Password Has Been Updated Successfully"})
        except:
            return {"message":"Error While Updating The password"},500


    def createNewUser(self,firstName="",lastName="",email="",password=""):
        receviedPassword=bytes(password,encoding='utf-8')
        hashed = bcrypt.hashpw(receviedPassword,salt)
        password=hashed
        try:
            UserDataBase(firstName,lastName,email,password).add()
            return jsonify({"message":"User Created Successfully"})
        except:
            return {"message":"Error whille Creating The Account"},500

    def verifyUser(self,email,password):
        if not email:
            return jsonify({"message":"Please Enter The valid Email Address"})
        if not password or len(password)<5:
            return jsonify({"message":"Invalid credentials"})
        try:
            searchUser=UserDataBase(email=email).searchByEmail()
            if searchUser==None:
                return {"message":"Unable To Find The Account With Given Email Id"},404
        except:
            return {"message":"Some Internal Error Has Been Occured While Fetch The Details"},500
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



