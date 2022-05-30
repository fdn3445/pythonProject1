import numpy as np
import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 100)

es_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Penelope22'
engine.setProperty('voice',es_voice_id)

def es_hablo(msg):
    engine.say(msg)
    engine.runAndWait()

a = np.array(['ser','estar', 'hablar', 'estudiar', 'escuchar', 'trabajar', 'mirar', 'viajar'])

while True:
    b = random.randint(0,7)
    text = a([b])
    es_hablo({text})
    key = input('type word here: ')
    if key !='exit':
        print(key)
    else:
        exit()

    '''
    key = input('press s: ')
    if text !='exit' :
        b = random.randint(0, 7)
        print(a[b])
        es_hablo({text})
    else:
        exit(s)
    '''
