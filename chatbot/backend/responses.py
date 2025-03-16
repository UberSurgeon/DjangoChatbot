import random
import requests
# https://picsum.photos/seed/picsum/200/300

last_msg = ''

def bot_response(message):
    global last_msg
    message = message.lower()
    if last_msg != message:
        last_msg = message
        if message == "hello":
            return "HIIIII"
        elif message == "goodbye":
            return "GOOD BYE :)"
        elif message == "help":
            return """
            Command list:
            1.hello
            2.goodbye
            3.help
            4.gimme image
            5.tell me about [something]
            6.weather in [city]
        """
        elif message == "gimme image":
            return bot_response_image()
        elif message.startswith("tell me about "):
            message = message.replace("tell me about ", '')
            return f'<a href="https://en.wikipedia.org/wiki/{message}">Wikipedia article about {message}</a>'
        elif message.startswith("weather in "):
            message = message.replace("tell me about ", '')
            key = "ccf9ec888da24ca1b5c180606251603"
            response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={message}&aqi=no")
            response = response.json()
            decoded = response
            decoded = decoded["current"]["temp_c"]
            
            return f'{decoded} C'
        else:
            return "OvO i dont know that"
    return "STOP REPEATING YOURSELF!"

def bot_response_image():
    seed = random.random()
    return f'<img src="https://picsum.photos/seed/{seed}picsum/200/300" alt="Description of Image">'
