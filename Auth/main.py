from flask import Flask
from flask_restful import Api
from database.mongoDB_AccessToken import cluster
from resources.user import AccessToken
app=Flask(__name__)
api=Api(app)

api.add_resource(AccessToken,"/access")

if __name__=="__main__":
    try:
        print("Connecting to the Database.....")
        cluster.admin.command('ping')
        app.run("8081",debug=True)
    except Exception as e:
        print("Error Occured while trying to run the server{}".format(e))
    finally:
        print("Closing the connection with Database......")
        cluster.close()