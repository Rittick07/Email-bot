import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine= pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sarkarrittick123@gmail.com','Rittick@07')
    email = EmailMessage()
    email['From']= 'sarkarrittick123@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'user': 'monishaarupsarkar@gmail.com',
    'account': 'ritticksarkar21@gmail.com'
}

def get_email_info():
    talk('To whom you Want to send email')
    name= get_info()
    receiver=email_list[name]
    print(receiver)
    talk('What is the subject of your email')
    subject=get_info()
    talk('Tell me the content of the email')
    message= get_info()
    send_email(receiver,subject,message)
    talk('Hey lazy ass your email is sent.')
    talk('Do you want to send any more emails?')
    send_more= get_info()
    if 'yes' in send_more:
        get_email_info()



get_email_info()