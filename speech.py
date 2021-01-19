import time
import speech_recognition as sr
import webbrowser
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# webdriver setup
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("window-size=1280,800")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
driver = webdriver.Chrome(executable_path='/home/heavy_rain/Pulpit/chromedriver', options=options)
driver.get('https://ttsmp3.com/text-to-speech/Polish/')

# function that converts text to speach
def igor_talk(phrase):
    # input clear input field and put my text
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "voicetext")))
    text_input = driver.find_element(By.ID, 'voicetext')
    text_input.clear()
    text_input.send_keys(phrase)

    # play text
    driver.find_element(By.ID, 'vorlesenbutton').click()
    time.sleep(5)

# speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic:
        try:
            print('Yes my Master...?:> ')   # use play sound for that
            mic_audio = r.listen(mic)       # listen on microphone for input
            mic_data = r.recognize_google(audio_data=mic_audio, language='pl-PL')   # google voice recognition service - wait till finish

            if 'szukaj' in mic_data:
                igor_talk('Co wyszukać')
                search_audio = r.listen(mic)
                search_data = r.recognize_google(audio_data=search_audio, language='pl-PL')
                webbrowser.open_new('https://www.google.com/search?q=' + search_data)
                igor_talk('Zrobione szefie')

            if 'pogoda' in mic_data:
                igor_talk('Gdzie?')
                weather_audio = r.listen(mic)
                weather_data = r.recognize_google(audio_data=weather_audio, language='pl-PL')
                weather_key = '8cbfad668c33b1bdce19655af03e5458'
                weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=pl'.format(weather_data, weather_key)
                weather_response = requests.get(weather_url)
                weather_response_data = json.loads(weather_response.text)
                weather_description = []
                for d in weather_response_data["weather"]:
                    weather_description.append(d["description"])
                igor_talk('Temperatura wynosi {} stopni... a odczuwalna temperatura to {}... warunki panujące na zewnątrz to {}'.format(weather_response_data["main"]["temp"], weather_response_data["main"]["feels_like"], weather_description))


        except sr.UnknownValueError:        # error handling - unknown command
            # igor_talk('Nie rozumiem mój panie')
            pass
        except sr.RequestError:             # error handling - connection problem
            igor_talk('Problemy z połączeniem mój panie')




