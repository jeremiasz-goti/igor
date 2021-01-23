import listen
import icmd
import speech_recognition as sr


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
                # search google
                if 'szukaj' in command:
                    icmd.igor_search()
                # search for weather
                if 'pogoda' in command:
                    icmd.igor_weather()
            # error handling - unknown command
            except sr.UnknownValueError:
                print('Nie rozumiem polecenia')
            # error handling - problem with request
            except sr.RequestError:
                print('request error')
    # error handling - no wake word            
    except TypeError:
        print('brak komend')