import datetime

def Action(data):
    if data is None:
        return "No input received"
    
    user_data = data.lower()

    if "time" in user_data:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
