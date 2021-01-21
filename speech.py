import time
import speech_recognition as sr
import webbrowser
import requests
import json
from gtts import gTTS




def igor_talk(phrase):
    tts = gTTS('hello')
    tts.save('hello.mp3')




def igor_listen():
    try:
        with sr.Microphone() as mic:
            mic_audio = r.listen()
            mic_data = r.recognize_google(language='pl-PL')
            return mic_data
    except sr.UnknownValueError:
        print('Nie rozumiem polecenia')
    except sr.RequestError:
        print('request error')


# speech recognition
r = sr.Recognizer()

# while True:

#     if 'szukaj' in mic_data:
#         igor_talk('Co wyszukać')
#         search_audio = r.listen(mic)
#         search_data = r.recognize_google(
#             audio_data=search_audio, language='pl-PL')
#         webbrowser.open_new('https://www.google.com/search?q=' + search_data)
#         igor_talk('Zrobione szefie')

#     if 'pogoda' in mic_data:
#         igor_talk('Gdzie?')
#         weather_audio = r.listen(mic)
#         weather_data = r.recognize_google(
#             audio_data=weather_audio, language='pl-PL')
#         weather_key = '8cbfad668c33b1bdce19655af03e5458'
#         weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(
#             weather_data, weather_key)
#         weather_response = requests.get(weather_url)
#         weather_response_data = json.loads(weather_response.text)
#         weather_description = []
#         for d in weather_response_data["weather"]:
#             weather_description.append(d["description"])
#         igor_talk('Temperatura wynosi {} stopni... a odczuwalna temperatura to {}... warunki panujące na zewnątrz to {}'.format(
#             weather_response_data["main"]["temp"], weather_response_data["main"]["feels_like"], weather_description))
igor_talk('cos')