import mysql.connector
import bcrypt

mydb=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="mysql",database="users")
Insert="INSERT INTO users (FistName, LastName, Email,Password) VALUES (%s, %s, %s,%s)"

class UserDataBase:
    def __init__(self,firstname,lastname,email,password):
        self.FirstName=firstname
        self.LastName=lastname
        self.Email=email
        self.Password=password
    
    def add(self):
        hashedPassword=bcrypt.hashpw(self.Password.encode('utf-8'),bcrypt.gensalt())
        self.Password=hashedPassword
        cur=mydb.cursor()
        cur.execute(Insert,self)
        cur.commit()
        cur.close()

    def searchByEmail(self):
        cur=mydb.cursor()
        return {"message":"Hello world"}
    def verifyUser(self):
        pass
    def deleteUser(self):
        pass

    def editUser(self):
        pass



    

