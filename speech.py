import os

import speech_recognition as sr
import webbrowser
import requests
import json
from gtts import gTTS
import playsound
from random import randint

def igor_talk(phrase):
    tts = gTTS(text=phrase, lang='pl')
    igor_response = r'audio/dynamic/' + (str(randint(0,999))) + '.mp3'
    igor_audio = tts.save(savefile=igor_response)
    playsound.playsound(igor_response)
    os.remove(path=igor_response)

def igor_listen():
    try:
        with sr.Microphone() as mic:
            mic_audio = r.listen(mic)
            mic_data = r.recognize_google(mic_audio, language='pl-PL')
            return mic_data
    except sr.UnknownValueError:
        igor_talk('Nie rozumiem polecenia')
    except sr.RequestError:
        igor_talk('request error')


# speech recognition
r = sr.Recognizer()

while True:
    mic_data = igor_listen()
    if 'szukaj' in mic_data:
        igor_talk('Co wyszukać')
        search_data = igor_listen()
        webbrowser.open_new('https://www.google.com/search?q=' + search_data)
        igor_talk('Zrobione szefie')

    if 'pogoda' in mic_data:
        igor_talk('Gdzie?')
        weather_audio = r.listen(mic)
        weather_data = r.recognize_google(
            audio_data=weather_audio, language='pl-PL')
        weather_key = '8cbfad668c33b1bdce19655af03e5458'
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(
            weather_data, weather_key)
        weather_response = requests.get(weather_url)
        weather_response_data = json.loads(weather_response.text)
        weather_description = []
        for d in weather_response_data["weather"]:
            weather_description.append(d["description"])
        igor_talk('Temperatura wynosi {} stopni... a odczuwalna temperatura to {}... warunki panujące na zewnątrz to {}'.format(
            weather_response_data["main"]["temp"], weather_response_data["main"]["feels_like"], weather_description))
