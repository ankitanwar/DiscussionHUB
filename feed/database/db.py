from pymongo import MongoClient

try:
    cluster=MongoClient(host="localhost",port=27017)
    db=cluster["feeds"]
    collection=db["feeds"]
except Exception as e:
    print("Error While connecting to the databse {}".format(e))



def PostContent(userID,userName,content):
    filter={"_id":userID}
    add={'$push':{"Content":content}}
    response=collection.update(filter,add,upsert=True)
    return response


def DeleteContent():
    pass
#gotta figure out some way to access the content uniquely


def ModifyContent():
    pass
#gotta figure out some way to access the content uniquely


def ViewContent(userID):
    filter={"_id":userID}
    result=collection.find_one(filter)
    return result

