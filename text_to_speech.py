import pyttsx3

def text_to_speech(text):
    
    engine = pyttsx3.init()
    #set speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-300')
    
    #get the available voices 
    voices = engine.getProperty('voices')
    #set the female voice
    engine.setProperty('voice', voices[1].id)
    
    #say the text
    engine.say(text)
    engine.runAndWait()

text_to_speech("hello jyothi....how can you help you today")