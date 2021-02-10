from flask_restful import Resource,reqparse
from flask import request
from pymongo import database
from database.mongoDB_AccessToken import AccessTokenDB
import requests

class AccessToken(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("email")
    parser.add_argument("password")

    def post(self):
        data=AccessToken.parser.parse_args()
        verify=requests.post("http://127.0.0.1:8080/verify",json={"email":data["email"],"password":data["password"]})
        if verify.status_code<=200:
            pass
        else:
            return {"message":
    
    def get(self):
        accessToken=request.headers.get("x-access-token")
        email=request.headers.get("email")
        if email=="":
            return {"message":"Invalid email address"}
        if accessToken=="":
            return {"message":"Invalid access token"}
        result=AccessTokenDB(email=email).verifyAccessToken()
        if result==None:
            return {"message":"Invalid Credentials please log in again"}
        if result["access_token"]!=accessToken:
            return {"message":"Invalid Access Token"}
        return {"message":"verified"}

