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
        verify=requests.post("http://127.0.0.1:8080/verify",json={"email":data["email"],"password":data["password"]})
        if verify.status_code<299:
            response=verify.json()
        else:
            return jsonify({"message":"Invalid credentials"})
        token=service.createAccessToken(userID=response["id"],email=response["email"],firstName=response["firstName"])
        return token
    
    def get(self):
        accessToken=request.headers.get("access_token")
        userID=request.headers.get("userID")
        response=service.verifyAccessToken(accessToken,userID)
        return response

