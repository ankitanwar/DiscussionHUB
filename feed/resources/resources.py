from flask_restful import Resource,reqparse
from flask import request
from services.services import FeedService
import requests

class Feed(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("content",type=str)
    
    def post(self):
        userID=request.headers.get("userID")
        accessToken=request.headers.get("access_token")
        headers={"userID":userID}
        verify=requests.get("http://127.0.0.1:8082/access",headers=request.headers)
        if verify.status_code<299:
            respones=verify.json()
            print("The value of response is",respones)
            return
        if userID=="":
            return {"message":"Invalid User ID"}
        if accessToken=="":
            return {"message":"Invalid token ID"}
        data=Feed.parser.parse_args()
        if data["content"]=="":
            return {"message":"Inavlid Content To Post"}
        userName="Testing"
        result=FeedService().addNewContent(userName,userID,data["content"])
        return result
        
        

    def delete(self):
        pass


class getContent(Resource):
    
    def get(self,memberID):
        response=FeedService().ViewAllContentOfParticularUser(memberID)
        return response