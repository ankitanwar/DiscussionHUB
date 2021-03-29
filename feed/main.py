from flask import Flask
from flask_restful import Api
from resources.resources import Feed,modifyContent,Ping

app=Flask(__name__)
api=Api(app)
api.add_resource(Feed,"/feed")
api.add_resource(modifyContent,"/feed/<string:postID>")
api.add_resource(Ping,"/ping")


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8070,debug=True)
