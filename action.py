import text_to_speech
import speech_to_text
import datetime
import webbrowser
import os

def Action(data):
    if data is None:
        return "No input received"
    user_data = data.lower()
    
    
                              
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual assistant")
        return 'My name is Virtual assistant'
    
    elif "hello" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech("hey, sir how can i help you")
        return "hey hii,how can i help you"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning madam")
        return "good morning madam"
    
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok madam")
        return "ok madam"
    
    elif "play music" in user_data:
        webbrowser.open("https://spotify.com")
        text_to_speech.text_to_speech("spotify.com is now ready for you.")
        return "spotify.com is now ready for you."
    
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("youtube.com is now ready for you.")
        return "youtube.com is now ready for you."
    
    elif "open google" in user_data:
        webbrowser.open("www.google.com")
        text_to_speech.text_to_speech("google.com is now ready for you.")
        return "google.com is now ready for you."
    
    elif "open weather" in user_data:
        webbrowser.open("https://www.google.com/search?q=weather")
        text_to_speech.text_to_speech("weather.com is now ready for you")
        return "weather.com is now ready for you"
    
    elif "current time" in user_data:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        text_to_speech.text_to_speech(f"The current time is {current_time}")
        return f"The current time is {current_time}"
    
    elif "open notepad" in user_data:
        os.system("notepad.exe")
        text_to_speech.text_to_speech("Opening Notepad...")
        return "Opening Notepad..."
    elif " " in user_data:
        query = user_data.replace(" ", " ").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        #text_to_speech.text_to_speech("Searching for {query} on Google...")
        #return f"Searching for {query} on Google.."
        response_text = f"Searching for {query} on Google..."
        text_to_speech.text_to_speech(response_text)  # Convert text to speech
        return response_text
    
    
    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"

        

    