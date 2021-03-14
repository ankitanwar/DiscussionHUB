from flask_restful import Resource,reqparse
from flask import request,jsonify
import requests
from functools import wraps
from services.services import FeedService

def authenticateUser(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        url="http://127.0.0.1:8082/access"
        req=requests.get(url,headers=request.headers)
        response=req.json()
        if response["message"]!="valid":
            return jsonify({"message":"Invalid Token ID"})
        return f(*args,**kwargs)
    return decorated


class Feed(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("content",type=str)
    
    def post(self):
        userID=request.headers.get("userID")
        userName="testing"
        data=request.get_json()
        if not data:
            return {"message":"Invalid Request"}, 400
        response=FeedService().addNewContent(userID,userName,data)
        return response

class getContent(Resource):
    
    def get(self,memberID):
        response=FeedService().ViewContentOfUser(memberID)
        return response
    

class modifyContent(Resource):

    def patch(self,postID):
        pass
    
    def delete(self,postID):
        userID=request.headers.get("userID")
        response=FeedService().deleteContent(userID,postID)
        return response
    
    def get(self,postID):
        response=FeedService().getPost(postID)
        return response


class filterContent(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("experience")
    parser.add_argument("role")
    parser.add_argument("company")

    def get(self):
        pass
