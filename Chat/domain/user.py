class User:
    def __init__(self,userID,Role):
        self.userID=userID
        self.Role=Role


class Room:
    def __init__(self,name,members):
        self.name=name
        self.members=[]
