from flask import Flask
from flask_restful import Api
from Resources.user import User

app=Flask(__name__)
api=Api(app)
api.add_resource(User,"/user")
api.add_resource(UserVerify,"/verify")


if __name__ == '__main__':
    try:
        db.ping()
        print("Successfully Connected To The User database")
    except Exception as e:
        print("Error while connecting to the databse {}".format(e))
    try:
        print("starting the server.......")
        app.run(port=8080,debug=True)
    except Exception as e:
        print("Error while starting the server {}".format(e))
    finally:
        print("Closing the connection with the database......")
        db.close()