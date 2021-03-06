from flask import Flask
from flask_restful import Api
from Resources.user import User,UserVerify
from DataBase.sqlDataBase import db,CreateTable

app=Flask(__name__)
api=Api(app)
api.add_resource(User,"/user")
api.add_resource(UserVerify,"/verify")

@app.before_first_request
def create_table():
    CreateTable()


if __name__ == '__main__':
    try:
        print("starting the server.......")
        app.run(host="0.0.0.0",port=8080,debug=True)
    except Exception as e:
        print("Error while starting the server {}".format(e))
    finally:
        print("Closing the connection with the database......")
        db.close()