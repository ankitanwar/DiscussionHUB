from flask_restful import Resource,reqparse
from flask import request,jsonify
import requests
from functools import wraps
from services.services import FeedService
from domain.domain import FeedDomain

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
    parser.add_argument("experience",type=str,required=True,help="Please Enter The Experience It could be Intern/1year/2year etc")
    parser.add_argument("role",type=str,required=True,help="Please Enter The type of role you are posting for")
    parser.add_argument("company",type=str,required=True,help="Please Add The Name Of The Company")
    parser.add_argument("description",type=str)

    #To post the new content
    def post(self):
        userID=request.headers.get("X-USER-ID")
        userName="testing"
        details=Feed.parser.parse_args()
        feed=FeedDomain(details["company"],details["role"],details["description"],details["experience"],userID,userName)
        response=FeedService().addNewContent(feed)
        return response
    
    #To view all the content of particular user they have posted
    def get(self):
        data=request.get_json()
        userID=data["userID"]
        response=FeedService().ViewContentOfUser(userID)
        return response

    

class modifyContent(Resource):

    #Allow user to modify the content they have posted
    def patch(self,postID):
        userID=request.headers.get("X-USER-ID")
        updatedDetails=request.get_json()
        feed=FeedDomain(updatedDetails["company"],updatedDetails["role"],updatedDetails["description"],updatedDetails["experience"],userID)
        response=FeedService().modifyContent(userID,postID,feed)
        return response
    
    #Allow user to delete the post they have posted
    def delete(self,postID):
        userID=request.headers.get("X-USER-ID")
        response=FeedService().deleteContent(userID,postID)
        return response
    

    #To view the particular post with the given ID
    def get(self,postID):
        response=FeedService().getPost(postID)
        return response


class filterContent(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("experience",type=str)
    parser.add_argument("role",type=str)
    parser.add_argument("company",type=str)

    #To filter the post according to the experience or role or by the company name
    def get(self):
        filters=filterContent.parser.parse_args()
        response=FeedService().filterPost(filters['experience'],filters["role"],filters["company"])
        return response
        
