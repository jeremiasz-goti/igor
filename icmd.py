import subprocess
import webbrowser
import requests
import json
import alsaaudio
from datetime import datetime, date
from youtubesearchpython import VideosSearch
import wikipedia



#   check time
def igor_time():
    # return current time
    return 'Jest {}'.format(datetime.utcnow().strftime("%H:%M"))

#   check date
def igor_date():
    # return current date
    return 'Dziś jest {}'.format(date.today().strftime('%d %B'))

#   search in google
def igor_search(search_data):
    # open webbrowser window and search for a given phrase in google
    webbrowser.open_new('https://www.google.com/search?q=' + search_data)
    # report finishing task
    return 'Wyszukiwanie zakończone'

#   check weather in given city
def igor_weather(location):
    # open weather api key
    weather_key = '8cbfad668c33b1bdce19655af03e5458'
    # open wather api endpoint
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(
        location, weather_key)
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

#   play youtube
def igor_youtube(youtube_search):
    youtube_search_result = VideosSearch(youtube_search, limit=1).result()
    webbrowser.open_new(youtube_search_result["result"][0]["link"])
    return ('Wyszukiwanie zakończone. Wyszukiwana fraza to: ' + youtube_search)

#   set system volume
def igor_volume(volume):
    am = alsaaudio.Mixer()
    base_volume = am.getvolume()
    if volume == 'głośniej':
            subprocess.call(["amixer", "-D", "pulse", "sset", "Master", str(base_volume[0] + 10 ) + '%'])
            print('Głośność: ' + str(base_volume[0]))
    if volume == 'ciszej':
            subprocess.call(["amixer", "-D", "pulse", "sset", "Master", str(base_volume[0] - 10 ) + '%'])
            print('Głośność: ' + str(base_volume[0]))


def igor_wikipedia(wikipedia_search):
    wikipedia.set_lang("pl")
    wikipedia_search_result = wikipedia.page(wikipedia_search)
    return (wikipedia_search_result.summary)

def igor_transport(bus_start, bus_stop):
    bus_url = 'https://jakdojade.pl/poznan/trasa/?fn={}&?tn={}'.format(bus_start, bus_stop)
    webbrowser.open_new(bus_url)

igor_transport('burysława','małe garbary')