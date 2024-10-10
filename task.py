import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import requests
import playsound
import webbrowser
import random

# Text-to-Speech (gTTS) ile metni seslendirme
def speak(text):
    tts = gTTS(text=text, lang='tr')
    filename = "temp_voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Seni dinliyorum...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='tr-TR')  # Türkçe komutları algıla
            print(f"Duyduğum: {command}")
            return command.lower()
        except Exception as e:
            print("Anlamadım, tekrar eder misin?")
            return ""

def get_weather():
    return "Hava durumu şu an kısmen güneşli."

def play_music():
    webbrowser.open("https://www.youtube.com/watch?v=0eGk7EAFErQ")  # Müslüm Gürses müziği

def get_exit_quote():
    quotes = [
        "Allaha emanet ol aslan parçası.",
       
    ]
    return random.choice(quotes)

def execute_command(command):
    if 'saat kaç' in command:
        current_time = datetime.datetime.now().strftime('%H:%M')
        speak(f"Saat şu anda {current_time}")
    elif 'hava durumu' in command:
        weather_info = get_weather()
        speak(weather_info)
    elif 'müzik aç' in command:
        speak("Müzik açılıyor.")
        play_music()
    elif 'solidworks aç' in command:
        speak("SolidWorks açılıyor.")
        os.startfile(r"C:\Users\LENOVO\OneDrive\Masaüstü\SOLIDWORKS 2018")  # SolidWorks'ün masaüstündeki kısayolu
    elif 'çıkış yap' in command or 'kapat' in command:
        exit_quote = get_exit_quote()
        speak(exit_quote)
        exit()
    else:
        speak("Bunu anlamadım, başka bir komut ver lütfen.")

if __name__ == "__main__":
    speak("Merhaba, Hoş geldin babayiğit nasıl yardımcı olabilirim?")
    while True:
        command = listen_command()
        execute_command(command)
