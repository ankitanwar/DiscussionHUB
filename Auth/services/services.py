import jwt
from flask import jsonify
import datetime
from flask import current_app as app
import database.accessTokenDB as db

def createAccessToken(userID,email,firstName):
    token=jwt.encode({'userID':userID, 'email':email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config["SECRET_KEY"])
    tokenID=token.decode('UTF-8')
    db.AccessToken().SaveAccessToken(email,userID,tokenID,firstName)
    return jsonify({"token":tokenID})

def verifyAccessToken(accessToken,userID):
    if not accessToken:
        return jsonify({"message":"Token is missing"})
    search=db.AccessToken().GetAccessToken(userID)
    if not search:
        return jsonify({"message":"Invalid Credentials"})
    savedToken=search["access_token"]
    if savedToken!=accessToken:
        return jsonify({"message":"Invalid Token ID"})
    if search["userID"]!=userID:
        return jsonify({"message":"Token Is Invalid"})
    try:
        _=jwt.decode(accessToken,app.config["SECRET_KEY"])
        return search
    except:
        return jsonify({"message":"Token Is Invalid"})


