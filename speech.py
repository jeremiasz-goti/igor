import time
import speech_recognition as sr
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

# function that converts text to speach
def igor_talk(phrase):
    # webdriver init
    driver.get('https://ttsmp3.com/text-to-speech/Polish/')

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
            print('Yes my Master...?:> ')
            mic_audio = r.listen(mic)
            mic_data = r.recognize_google(audio_data=mic_audio, language='pl-PL')
            igor_talk(mic_data)
        except sr.UnknownValueError:
            igor_talk('Nie rozumiem mój panie')
        except sr.RequestError:
            igor_talk('Problemy z połączeniem mój panie')






