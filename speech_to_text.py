import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    
        voice_data = " "
    try:
        voice_data = r.recognize_google(audio)
        
        return voice_data
    except sr.UnknownValueError:
        print("Hey Jyothi")
    except sr.RequestError:
        print("RequestError")
        
        
speech_to_text()
    
        
    
    
    
    
    
    
    
    