import PySimpleGUI as pg
import pyttsx3


engine = pyttsx3.init()

pg.theme('DarkBlack')
layout = [
    [pg.Text('Enter Text to Speak:', font=('Arial', 15)), pg.InputText(key='-INPUT-', font=('Arial', 15)), pg.Button('Speak', font=('Arial', 15))],
    [pg.Text('Select a Voice:', font=('Arial', 15)), pg.Radio('Male', "RADIO1", default=True, font=('Arial', 15), key='-MALE-'), pg.Radio('Female', "RADIO1", font=('Arial', 15), key='-FEMALE-')],
    [pg.Text('Adjust Volume:', font=('Arial', 15)), pg.Slider(range=(0, 100), default_value=50, orientation='h', size=(20, 15), font=('Arial', 15), key='-VOLUME-')],
    [pg.Text('Adjust Speed:', font=('Arial', 15)), pg.Slider(range=(100, 500), default_value=200, orientation='h', size=(20, 15), font=('Arial', 15), key='-SPEED-')],
    [pg.Button('Exit',font=('Arial', 15))]
]


window = pg.Window('Text-to-Speech App', layout )


def speak(text, volume, speed):
    # Setting the voice based on the user preference
    if values['-MALE-']:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    else:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)

   
    engine.setProperty('volume', volume / 100)
    engine.setProperty('rate', speed)

    
    engine.say(text)
    engine.runAndWait()


while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    if event in (pg.WINDOW_CLOSED, 'Exit'):
        break

    if event == 'Speak':
        text = values['-INPUT-']
        volume = values['-VOLUME-']
        speed = values['-SPEED-']
        speak(text, volume, speed)

window.close()