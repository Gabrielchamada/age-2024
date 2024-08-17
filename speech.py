import pyttsx3

#init of speech engine
engine = pyttsx3.init()

question = int(input("Sua idade: ")) #input of age
year = (2024 - question) #know what year of born

#say the message
engine.say(f'você nasceu em {year}') #use the "fprint" because that works
engine.runAndWait() #run the voice and close the voice