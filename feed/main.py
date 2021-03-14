from flask import Flask
from flask_restful import Api
from resources.resources import Feed,getContent,modifyContent

app=Flask(__name__)
api=Api(app)
api.add_resource(Feed,"/feed")
api.add_resource(getContent,"/feeds/<string:memberID>")
api.add_resource(modifyContent,"/feed/<string:postID>")


if __name__=="__main__":
    app.run(port=8070,debug=True)
