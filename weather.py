#getting wether info...
import requests, json
api_key = "63516f4651e2bc5384bae658843f6dd3"

base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + 'delhi'
response = requests.get(complete_url)

def weather():
        global response
        x = response.json()
        if x["cod"] != ("404"):
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
        return  current_temperature,current_humidiy,current_pressure


def tempreature():
    global response
    x = response.json()
    if x["cod"] != ("404"):
            y = x["main"]
            current_temperature = y["temp"]
    return current_temperature

def current_pressure():
    global response
    x = response.json()
    if x["cod"] != ("404"):
            y = x["main"] 

            current_pressure = y["pressure"]
    return current_pressure
def current_humidiy():
    global response
    x = response.json()
    if x["cod"] != ("404"):
            y = x["main"]
            current_humidiy = y["humidity"]
    return current_humidiy
