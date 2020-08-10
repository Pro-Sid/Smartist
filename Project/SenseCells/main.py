import sys
import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts
from GreyMatter import play_music

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

#Functioning Variable
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password']
music_path = profile_data['music_path']
play_music.mp3gen(music_path)

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

def main():

#obtain audio from microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

  try:
    speech_text = r.recognize_google(audio).lower().replace("'", "")
    print("Smartist thinks you said '" + speech_text + "'")

  except sr.UnknownValueError:
    print("Smartist could not understand audio")

  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service;{0}".format(e))

  brain(name,speech_text, city_name, city_code, proxy_username, proxy_password,  music_path)

main()

