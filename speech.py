import os
import speech_recognition as sr
import webbrowser
import requests
import json
import playsound
from gtts import gTTS
from random import randint


# speech recognition init
r = sr.Recognizer()

# takes string as an argument and sends it through google text to speech service
def igor_talk(phrase):
    # basic init
    tts = gTTS(text=phrase, lang='pl')
    # randomly generated file name path
    igor_response = r'audio/dynamic/' + (str(randint(0, 999))) + '.mp3'
    # saving mp3 file downloaded from gtts service to a given path
    igor_audio = tts.save(savefile=igor_response)
    # playing back response mp3 with playsound
    playsound.playsound(igor_response)
    # remove dynamic audio file
    os.remove(path=igor_response)

# listen for input on microphone
def igor_listen():
    with sr.Microphone() as mic:
        # listen for microphone audo
        mic_audio = r.listen(mic)
        # dump micropgone audio to text
        mic_data = r.recognize_google(mic_audio, language='pl-PL')
        # return speech to text
        return mic_data

# search in google
def igor_search(igor_listen):
    # listening for argument to search
    igor_talk('Co wyszukać')
    # save a string for searching to a variable
    search_data = igor_listen()
    # open webbrowser window and search for a given phrase in google
    webbrowser.open_new('https://www.google.com/search?q=' + search_data)
    # report finishing task
    igor_talk('Zrobione szefie')

# check weather in given city
def igor_weather(igor_listen):
    # listening for city to search
    igor_talk('Gdzie?')
    # save a city name in a variable
    weather_data = igor_listen()
    # open weather api key
    weather_key = '8cbfad668c33b1bdce19655af03e5458'
    # open wather api endpoint
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(
        weather_data, weather_key)
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
    igor_talk('Temperatura wynosi {} stopni... a odczuwalna temperatura to {}... warunki panujące na zewnątrz to {}'.format(weather_response_data["main"]["temp"], weather_response_data["main"]["feels_like"], weather_description))


while True:
    mic_data = igor_listen()
    # listen for wake word
    try:
        if 'igor' in mic_data:
        # respond to wake word
            igor_talk('Tak panie?')
        # listen for commands
            try:
        # search for text in google
                command = igor_listen()
                if 'szukaj' in command:
                    igor_search(igor_listen)
        # search for weather
                if 'pogoda' in command:
                    igor_weather(igor_listen)

        # error handling - unknown command
            except sr.UnknownValueError:
                igor_talk('Nie rozumiem polecenia')
        # error handling - problem with request    
            except sr.RequestError:
                igor_talk('request error')
    # error handling - unknown command
    except sr.UnknownValueError:
        igor_talk('Nie rozumiem polecenia')
    # error handling - problem with request    
    except sr.RequestError:
        igor_talk('request error')
