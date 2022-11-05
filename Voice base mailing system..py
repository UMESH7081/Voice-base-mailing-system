import speech_recognition as sr 
import smtplib 
import pyttsx3 

recognizer=sr.Recognizer() 
engine = pyttsx3.init() 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 


def talk(text): 
    engine.say(text)
    engine.runAndWait()

text=""
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    recognizer.energy_threshold=1200
    print("Speak the message")
    talk("Speak the message")

    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    
    print('Your message:{}'.format(text))      
    

except Exception as ex:
    print(ex)


message=text                                                         
talk(message)          
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('xyz@gmail.com','password')  
server.sendmail('xyz@gmail.com','receiver mail id',message) 
server.close()
print("Email Sent")
talk("Email Sent")
    
