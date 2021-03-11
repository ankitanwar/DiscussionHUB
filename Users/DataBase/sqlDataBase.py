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
SEARCHBYMAIL="SELECT * FROM user WHERE email = %s"
DELETE="DELETE FROM user WHERE email = %s"
UPDATE="UPDATE user SET firstname=%s,lastname=%s,email=%s WHERE id=%s"
UPDATEPASSWORD="UPDATE user SET password=%s WHERE id=%s"
SEARCHBYID="SELECT * FROM user WHERE id = %s"


class UserDataBase:
    def __init__(self,firstname="",lastname="",email="",password=""):
        self.firstname=firstname
        self.Password=password
        self.email=email
        self.lastname=lastname

    def add(self):
        data=(self.firstname,self.lastname,self.email,self.Password)
        cursor.execute(INSERT,data)
        db.commit()

    def searchByEmail(self):
        email=(self.email,)
        cursor.execute(SEARCHBYMAIL,email)
        found=cursor.fetchone()
        if found:
            return found

    def searchByID(self,id):
        cursor.execute(SEARCHBYID,id)
        found=cursor.fetchone()
        if found:
            return found
            
    def deleteUser(self):
        email=(self.email,)
        cursor.execute(DELETE,email)
        db.commit()


    def updateDetails(self,id):
        data=(self.firstname,self.lastname,self.email,id)
        cursor.execute(UPDATE,data)
        db.commit()

    def updatePassword(self,userID):
        data=(self.Password,userID)
        cursor.excute(UPDATEPASSWORD,data)
        db.commit()


    

