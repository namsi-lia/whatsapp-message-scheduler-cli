from twilio.rest import Client
import os

def schedule_message(message,number):
    account_sid =  'ACc0418760bcc77f170e9210571dd1073b'
    auth_token = '687af050011e5f8d04e13ca1ad96b79e'
    client = Client(account_sid, auth_token) 
    number = str(number)
    
    message = client.messages.create( 
                               from_='whatsapp:+14155238886',  
                              body=message,      
                              to='whatsapp:+'+number 
                              
                            )
    print(message.sid)
                        