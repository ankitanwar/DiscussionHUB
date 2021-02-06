import bcrypt
import mysql.connector

try:
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="user",
    )
    cursor=db.cursor(buffered=True)
except Exception as e:
    print("Error while connecting to the user database {}".format(e))
INSERT="INSERT INTO user (firstname,lastname,email,password) VALUES (%s,%s,%s,%s)"
SEARCH="SELECT * FROM user WHERE email = %s"


class UserDataBase:
    def __init__(self,firstname="",lastname="",email="",password=""):
        self.firstname=firstname
        self.Password=password
        self.email=email
        self.lastname=lastname

    def add(self):
        hashedPassword=bcrypt.hashpw(self.Password.encode('utf-8'),bcrypt.gensalt())
        self.Password=hashedPassword
        data=(self.firstname,self.lastname,self.email,self.Password)
        cursor.execute(INSERT,data)
        db.commit()

    def searchByEmail(self):
        email=(self.email,)
        cursor.execute(SEARCH,email)
        found=cursor.fetchone()
        if found:
            return found
    def verifyUser(self,email,password):
        search=db.session.query(UserDataBase).filter(UserDataBase.Email==email).first()
        if search:
            return search
    def deleteUser(self):
        pass

    def editUser(self):
        pass



    

