from flask import Flask
from flask_restful import Api
from user.user import User
from db import db

app=Flask(__name__)
api=Api(app)
db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3307/testdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api.add_resource(User,"/user")


if __name__ == '__main__':
    app.run(port=8080,debug=True)