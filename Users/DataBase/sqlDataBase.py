import bcrypt
from db import db

class UserDataBase(db.Model):
    __tablename__='users'
    FistName=db.Column(db.Integer,primary_key=True)
    LastName=db.Column(db.String(50))
    Email=db.Column(db.String(50),unique=True,nullable=False)
    Password=db.Column(db.String(50),nullable=False)

    def add(self):
        print("This is working")
        hashedPassword=bcrypt.hashpw(self.Password.encode('utf-8'),bcrypt.gensalt())
        self.Password=hashedPassword
        db.session.add(self)
        db.session.commit()

    def searchByEmail(self,email):
        search=db.session.query(UserDataBase).filter(UserDataBase.Email==email).first()
        if search:
            return search
    def verifyUser(self):
        pass
    def deleteUser(self):
        pass

    def editUser(self):
        pass



    

