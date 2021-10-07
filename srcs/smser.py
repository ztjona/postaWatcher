# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
06 / 10 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

def sendSMS(txt: str)->bool:
    '''Sends an sms with the given txt
    Returns true when ok
    ############################################### '''
    

    from twilio.rest import Client 

    from os import getenv 
    account_sid = getenv('TWILIO_SID')
    auth_token = getenv('TWILIO_TOKEN') 
    client = Client(account_sid, auth_token) 
    
    serviceID = getenv('serviceID')
    phoneNum = getenv('phoneNum')
    message = client.messages.create(  
                                messaging_service_sid=serviceID, 
                                body=txt,      
                                to=phoneNum)
    
    print(message.sid)
    return True
