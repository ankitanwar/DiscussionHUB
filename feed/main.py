from flask import Flask
from flask_restful import Api
from resources.resources import Feed,getContent

app=Flask(__name__)
api=Api(app)
api.add_resource(Feed,"/feed")
api.add_resource(getContent,"/feed/<string:memberID>")


if __name__=="__main__":
    app.run(port=8070,debug=True)
