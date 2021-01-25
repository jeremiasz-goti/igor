import webbrowser
import requests
import json
from datetime import datetime, date
from bs4 import BeautifulSoup


# check time
def igor_time():
    # return current time
    return 'Jest {}'.format(datetime.utcnow().strftime("%H:%M"))

# check date
def igor_date():
    # return current date
    return 'Dziś jest {}'.format(date.today().strftime('%d %B'))

# search in google
def igor_search(search_data):
    # open webbrowser window and search for a given phrase in google
    webbrowser.open_new('https://www.google.com/search?q=' + search_data)
    # report finishing task
    return 'Wyszukiwanie zakończone'

# check weather in given city
def igor_weather(location):
    # open weather api key
    weather_key = '8cbfad668c33b1bdce19655af03e5458'
    # open wather api endpoint
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(
        location, weather_key)
    # send request to weather api
    weather_response = requests.get(weather_url)
    # load api response to a json file
    weather_response_data = json.loads(weather_response.text)
    # creating list for weather conditions to append to
    weather_description = []
    # loop through weather conditions
    for d in weather_response_data["weather"]:
        # append weather conditions to list
        weather_description.append(d["description"])
    # return weather to speak function
    return 'Temperatura wynosi {} stopni... a odczuwalna temperatura to około {} stopnia... warunki panujące na zewnątrz to {}'.format(
        weather_response_data["main"]["temp"], str(round(weather_response_data["main"]["feels_like"], 1)), weather_description)

# def igor_shopping(shopping_item):
#     shopping_list = []
#     shopping_list.append(shopping_item)
#     return shopping_list

# play youtube
# def igor_youtube(youtube_search):
#     base_url = requests.get('https://www.youtube.com/results?search_query={}'.format(youtube_search))
#     soup = BeautifulSoup(base_url, 'html.parser')
#     print(soup)



