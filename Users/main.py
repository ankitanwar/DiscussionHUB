from flask import Flask
from flask_restful import Api
from user.user import User

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(User,"/user")


if __name__ == '__main__':
    app.run(port=8080,debug=True)