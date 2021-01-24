import speech_recognition as sr

# speech recognition init
r = sr.Recognizer()

# listen for input on microphone
def igor_listen():
    # use microphone as input
    with sr.Microphone() as mic:
        try:
            # listen for microphone audo
            mic_audio = r.listen(mic)
            # dump micropgone audio to text
            mic_data = r.recognize_google(mic_audio, language='pl-PL')
            # return speech to text
            return mic_data
        # error handling - unknown command
        except sr.UnknownValueError:
            print('Nie rozumiem polecenia')
            pass
        # error handling - problem with request
        except sr.RequestError:
            print('request error')

