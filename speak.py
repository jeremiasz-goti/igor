import os
import playsound
from gtts import gTTS
from random import randint

# takes string as an argument and sends it through google text to speech service
def igor_speak(phrase):
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

