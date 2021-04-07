from flask_restful import Resource,reqparse
from flask import request,jsonify
import requests
import services.services as service

class AccessToken(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("email")
    parser.add_argument("password")

    def post(self):
        response=None
        data=AccessToken.parser.parse_args()
        try:
            verify=requests.post("http://user:8080/verify",json={"email":data["email"],"password":data["password"]})
        except:
            return {"message":"Error While trying to verify email ID and password"},500
        if verify.status_code<299:
            response=verify.json()
        else:
            return jsonify({"message":"Invalid credentials"})
        token=service.createAccessToken(userID=response["id"],email=response["email"],firstName=response["firstName"])
        return token
    
    def get(self):
        accessToken=request.headers.get("X-Token-ID")
        userID=request.headers.get("X-Caller-ID")
        response=service.verifyAccessToken(accessToken,userID)
        return response

    def delete(self):
        accessToken=request.headers.get("X-Token-ID")
        userID=request.headers.get("X-Caller-ID")
        response=service.delete_access_token(userID,accessToken)
        return response

