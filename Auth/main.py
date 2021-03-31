from flask import Flask
from flask_restful import Api
from database.accessTokenDB import cluster
from resources.user import AccessToken

app=Flask(__name__)
api=Api(app)
app.config["SECRET_KEY"]="thisisthesecretkey"
api.add_resource(AccessToken,"/access")

if __name__=="__main__":
    try:
        print("Connecting to the Database.....")
        cluster.admin.command('ping')
        app.run(host="0.0.0.0",port="8082",debug=True)
    except Exception as e:
        print("Error Occured while trying to run the server{}".format(e))
    finally:
        print("Closing the connection with Database......")
        cluster.close()