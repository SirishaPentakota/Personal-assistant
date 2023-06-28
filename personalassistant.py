import speech_recognition as sr
import pyttsx3 
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki


listener = sr.Recognizer()
speaker = pyttsx3.init()


rate=speaker.getProperty('rate')
speaker.setProperty('rate',190)

'''
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
'''


name='jarvis'


def speak(text):
    speaker.say('Yes madam' + text)
    speaker.runAndWait()

speak('Iam your '+ name +'Tell me madam')


def take_command():
    try:
        
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            if name in command:
                command= command.replace(name + '','')
               # print(command)
                #speak(command)
               
    except:
        print('Check your Microphone')
    return command

while True:
    user_command = take_command()
    print(user_command)
    speak(user_command)
    if 'close' in user_command:
        print('See you again madam. I will be there when ever you call me')
        speak('See you again madam. I will be there when ever you call me')
        
        break
    elif 'time' in user_command:
        curr_time=dt.datetime.now().strftime("%I:%M %p")
        
        print(curr_time)
        speak(curr_time)

    elif 'open' in user_command:
        user_command = user_command.replace('play ','')
        
        print('playing'+ user_command)
        speak('playing'+ user_command+',engoy madam.')
        pk.playonyt(user_command)
        break
    
    elif 'search for ' in user_command:
        user_command = user_command.replace('search for','')
        user_command = user_command.replace('google','')
        speak('Searching for'+ user_command)
        pk.search(user_command)

    elif 'who is ' in user_command:
        user_command = user_command.replace('who is ','')
        info = wiki.summary(user_command,5)
        print(info)
        speak(info)
    

    
            
        



take_command()

    
        
    
