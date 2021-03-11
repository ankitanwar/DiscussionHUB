import jwt
from flask import jsonify
import datetime
from flask import current_app as app
import database.accessTokenDB as db

def createAccessToken(userID,email,firstName):
    token=jwt.encode({'userID':userID, 'email':email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config["SECRET_KEY"])
    tokenID=token.decode('UTF-8')
    try:
        db.AccessToken().SaveAccessToken(email,userID,tokenID,firstName)
        return jsonify({"token":tokenID})
    except:
        return {"message":"Error While Creating The New Access Token"},500

def verifyAccessToken(accessToken,userID):
    if not accessToken:
        return jsonify({"message":"Token is missing"})
    try:
        search=db.AccessToken().GetAccessToken(userID)
    except:
        return {"message":"Error while fetching the details"},500
    if not search:
        return {"message":"Invalid Credentials"}, 404
    savedToken=search["access_token"]
    if savedToken!=accessToken:
        return {"message":"Invalid Token ID"}, 404
    if search["_id"]!=int(userID):
        return {"message":"Token Is Invalid"}, 404
    try:
        _=jwt.decode(accessToken,app.config["SECRET_KEY"])
        return jsonify({"message":"valid","userID":search["_id"],"email":search["email"]})
    except:
        return {"message":"Token Is Invalid"}, 404


