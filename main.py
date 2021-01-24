import listen
import icmd
import speech_recognition as sr
import speak
import icmd


while True:
    print("slucham")
    # listen for wake word
    word = listen.igor_listen()
    try:
        # if wake word is activated, start giving cmmands   
        if 'ahoj' in word:
            print('rozkazuj')
            try:
                # give voice command to trigger functions
                command = listen.igor_listen()
                # report current time
                if 'godzina' in command:
                    time_report = icmd.igor_time()
                    speak.igor_speak(time_report)
                # report current date
                if 'dzień' in command:
                    date_report = icmd.igor_date()
                    speak.igor_speak(date_report)
                # open search in google
                if 'szukaj' in command:
                    speak.igor_speak('Co wyszukać')
                    search = listen.igor_listen()
                    search_report = icmd.igor_search(search)
                    speak.igor_speak(search_report)
                # report  weather
                if 'pogoda' in command:
                    speak.igor_speak('Gdzie')
                    location = listen.igor_listen()
                    weather_report = icmd.igor_weather(location)
                    speak.igor_speak(weather_report)
            # error handling - unknown command
            except sr.UnknownValueError:
                print('Nie rozumiem polecenia')
            # error handling - problem with request
            except sr.RequestError:
                print('request error')
    # error handling - no wake word            
    except TypeError:
        print('brak komend')