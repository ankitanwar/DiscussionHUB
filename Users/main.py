from flask import Flask
from flask_restful import Api
from Resources.user import User,UserLogin
from DataBase.sqlDataBase import db

app=Flask(__name__)
api=Api(app)
api.add_resource(User,"/user")
api.add_resource(UserLogin,"/login")


if __name__ == '__main__':
    try:
        db.ping()
        print("Successfully Connected To The User database")
    except Exception as e:
        print("Error while connecting to the databse {}".format(e))
    app.run(port=8080,debug=True)