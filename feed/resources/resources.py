from flask_restful import Resource,reqparse
from flask import request,jsonify
from services.services import FeedService
import requests
from functools import wraps

def getUserDetails(f):
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
    
    @getUserDetails
    def post(self):
        data=request.get_json()
        if not data:
            return {"message":"Invalid Request"}, 400
        
        
    @getUserDetails  #this is bascially to authenticate the request
    def delete(self):
        pass


class getContent(Resource):
    
    def get(self,memberID):
        response=FeedService().ViewAllContentOfParticularUser(memberID)
        return response