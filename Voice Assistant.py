import warnings
warnings.filterwarnings("ignore")


import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr
import pyowm

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']

question = ['how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]

var1 = ['who made you', 'who created you']
var2 = ['I was made by Anurag', 'Anurag', 'Some guy whom i never got to know.','It is confidential']

var3 = ['what time is it', 'what is the time', 'time']

var4 = ['who are you', 'what is your name']
name = ['I am Jarvis', 'I am your chatbot','I feel bad that you have forgotten me!!']

var5 = ['date','what date it is','what date is it','what is the date']

cmd1 = ['open browser', 'open Google']

cmd2 = ['play music', 'play songs','play song', 'play a song', 'open music player']

cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell me something funny']
jokes = ['Can a kangaroo jump higher than a house? \nOf course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. \nIt got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.\nPatient: What do you mean, 10? 10 what? Months? Weeks?\nDoctor: Nine. Eight. Seven. Six.\nPatient: Oh Lord!']

cmd4 = ['open youtube', 'I want to watch a video']

cmd5 = ['tell me the weather', 'weather', 'what about the weather']

cmd10 = ['search','search something','Google something']

cmd7 = ['what is your color', 'what is your colour', 'your colour', 'your colour?']
cmd8 = ['favourite colour', 'what is your favourite colour']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']

cmd9 = ['thank you','thanks','thanks a lot']
repfr9 = ['you are welcome', 'glad i could help you','mention not']

cmd6 = ['exit', 'close', 'goodbye', 'nothing','bye bye']

robo = '''
       ██████████████████       
    ████▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓███     
   ██▓▓█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█▓▓█    
  ██████████▓▓▓▓▓▓▓▓██████████  
  ██      ███████████       ██  
 ███       ██▓▓▓▓▓▓█        ███ 
 ████       █▓▓▓▓▓▓█       ████ 
 ██▓█       █▓▓▓▓▓▓█       █▓██ 
████▓█      █▓▓▓▓▓▓█      █▓████
█▓██▓█      ▀██████▀      █▓██▓█
█▓██▓█                    █▓██▓█
█▓████                    ████▓█
█▓██▀                      ▀██▓█
█▓██  █▀▀▀▀▄▄      ▄▄▀▀▀▀█  ██▓█
███   █     ▀██▄▄██▀     █   ███
 ██   ▀█▄▄▄▄█▀    ▀█▄▄▄▄█▀   ██ 
 ███                        ███ 
  █▓█                      █▓█  
  █▓▓█                    █▓▓█  
  █▓▓▓█                  █▓▓▓█  
  █▓▓▓▓█▄              ▄█▓▓▓▓█  
   █▓▓█▀█  ▄▀▀▀▀▀▀▀▀▄  █▀█▓▓█   
    █▓█ ▀▄▄▀        ▀▄▄▀ █▓█    
     █▓█     ▄▄▄▄▄▄     █▓█     
      █▓█▄▄▄██▓▓▓▓██▄▄▄█▓█      
       █▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█       
        ████████████████        

   _                  _     
  (_)                (_)    
   _  __ _ _ ____   ___ ___ 
  | |/ _` | '__\ \ / / / __|
  | | (_| | |   \ V /| \__ \
\n  | |\__,_|_|    \_/ |_|___/
 _/ |                       
|__/                        
'''

print(robo)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nTell me something:")
        audio = r.listen(source)
        try:
            user_said = r.recognize_google(audio)
            print("You said:- " + user_said)
        except sr.UnknownValueError:
            print("\nCould not understand audio. Run code again if problem persists.")
            engine.say('I didnt get that.')
            engine.runAndWait()
            continue
            
    if user_said in greetings:
        reply = random.choice(greetings)
        print(reply)
        engine.say(reply)
        engine.runAndWait()
        
    elif user_said in question:
        print('I am fine')
        engine.say('I am fine')
        engine.runAndWait()
        
    elif user_said in var1:
        reply = random.choice(var2)
        print(reply)
        engine.say(reply)
        engine.runAndWait()
        
        
    elif user_said in cmd9:
        reply = random.choice(repfr9)
        print(reply)
        engine.say(reply)
        engine.runAndWait()

        
    elif user_said in cmd7:
        reply = random.choice(colrep)
        print(reply)
        engine.say(reply)
        engine.runAndWait()
        print('It keeps changing every second. Uhm I am always so confused.')
        engine.say('It keeps changing every second. Uhm I am always so confused.')
        engine.runAndWait()
        
        
    elif user_said in cmd8:
        reply = random.choice(colrep)
        print(reply)
        engine.say(reply)
        engine.runAndWait()
        print('Let me tell you it keeps changing.')
        engine.say('Let me tell you it keeps changing.')
        engine.runAndWait()
        
    elif user_said in cmd2:
        webbrowser.open('https://music.youtube.com/watch?v=MC7_caN3yBA&list=RDAObHaAxpOZhcVmmF6I3y0siA')
        
    elif user_said in var4:
        reply = random.choice(name)
        print(reply)
        engine.say(reply)
        engine.runAndWait()
        
    elif user_said in cmd4:
        webbrowser.open('www.youtube.com')
        
    elif user_said in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
        
    elif user_said in cmd5:
        owm = pyowm.OWM('YOUR_API_KEY')
        observation = owm.weather_at_place('Bangalore, IN')
        observation_list = owm.weather_around_coords(12.972442, 77.580643)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()
        
    elif user_said in var3:
        now = datetime.datetime.now()
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()

    elif user_said in var5:
        now = datetime.datetime.now()
        print(now.date())
        engine.say(now.date())
        engine.runAndWait()
        
    elif user_said in cmd1:
        webbrowser.open('www.google.com')
        
    elif user_said in cmd3:
        reply = random.choice(jokes)
        print(reply)
        engine.say(reply)
        engine.runAndWait()

    elif user_said in cmd10:
        with sr.Microphone() as source:
            print("What do you want to search?")
            engine.say("What do you want to search?")
            engine.runAndWait()
            audio = r.listen(source)
            try:
                user_said = r.recognize_google(audio)
                reply = "You want to search " + user_said
                print(reply)
                engine.say(reply)
                engine.runAndWait()
                webbrowser.open_new('www.google.com/search?q=' + user_said)
            except sr.UnknownValueError:
                print("\nCould not understand audio. Run code again if problem persists.")
                engine.say('I didnt get that.')
                engine.runAndWait()
                continue
        
    else:
        engine.say("Please wait")
        engine.runAndWait()
        try:
            print(wikipedia.summary(user_said))
            engine.say(wikipedia.summary(user_said))
            engine.runAndWait()
        except wikipedia.exceptions.DisambiguationError as e:
            print('Please be more specific or choose from the below:\n')
            engine.say('Please be more specific or choose from the below:')
            engine.runAndWait()
            for i in range(len(e.options)):
                if i==5:
                    break
                print(e.options[i])
                engine.say(e.options[i])
                engine.runAndWait()
            with sr.Microphone() as source:
                print("\nWhat is your choice?")
                engine.say("What is your choice?")
                engine.runAndWait()
                audio = r.listen(source)
                try:
                    user_said = r.recognize_google(audio)
                    reply = "Your choice is " + user_said
                    print(reply)
                    engine.say(reply)
                    engine.runAndWait()
                    print(wikipedia.summary(user_said))
                    engine.say(wikipedia.summary(user_said))
                    engine.runAndWait()
                except sr.UnknownValueError:
                    print("\nUh oh! There seems to be something wrong.")
                    engine.say('I didnt get that.')
                    engine.runAndWait()
                    continue
        except Exception:
            print('Oops. Search something different!!')
            engine.say('I didnt get that.')
            engine.runAndWait()
            continue
