from flask_socketio import send
from sockets import socketio
from database.chatDatabase import chatDB


class ChatService:
    
    @socketio.on("send_message")
    def sendMessage(self,message,roomID):
        try:
            chatDB().saveMessage(roomID,message)
            socketio.emit('receive_message',message,roomID)
        except:
            return {"message":"Couldn't send the message please try again..."},500
    
    def getOlderMessages(self,roomID):
        try:
            messages=chatDB().fetchOlderMessages(roomID)
            return messages
        except:
            return {"message":"Couldn't Fetch The previous messages"},500
        

