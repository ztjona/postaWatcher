# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
21 / 05 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from os import getenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP


'''Module to send notification email.
# TUTORIAL
# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
################################################### '''
#----- CONFIGS

def newTweet(text:str)->str:
    '''returns body for mail
    ############################################### '''
    
    mail_content = '''TWITTER, se ha publicado el tweet!
    /////////////

    {}
    
    ////////////

    Atentamente----
    ztjona!
    '''.format(text)
    return mail_content



def exception_handler(func):
    '''try catch decorator
    ############################################### '''
    def inner_function(*args, **kwargs):
        try:
            resp = func(*args, **kwargs)
            return resp
        except Exception as e:
            print("No se pudo enviar mail!")
            print(e)
            return False
    return inner_function


@exception_handler
def twitterEmail(text:str) -> bool:
    '''Sends the notification email to the listener.
    True when ok, false, not ok.
    ############################################### '''

    #The SENDER email
    sender_address = getenv('SENDER', 'yo@atp.com')
    listener_address = getenv('LISTENER', 'yo@atp.com')
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = listener_address
    message['Subject'] = 'POSTA notifier: tweet found!'  # The subject line

    #The body and the attachments for the mail
    message.attach(MIMEText(newTweet(text), 'plain'))

    #Create SMTP session for sending the mail
    # session = SMTP('smtp.gmail.com', 587)  # use gmail with port
    session = SMTP('smtp-mail.outlook.com', 587)  # using hotmail account
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, getenv('MAILPASS', 'myClaveXD'))
    text = message.as_string()
    SendErrs = session.sendmail(sender_address, listener_address, text)
    print(SendErrs)
    session.quit()

    print('Mail Sent')
    return True  # false, en exception
