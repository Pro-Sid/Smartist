import time

from SenseCells.tts import tts

def countdown(speech_text):
  words_of_message = speech_text.split()
  words_of_message.remove('set')
  words_of_message.remove('timer')
  words_of_message.remove('for')
  cleaned_message = ' '.join(words_of_message)
  t, m = cleaned_message.split()
  t = int(t)
  t = t*60
  while t:
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins,secs)
    print(timeformat + '\n')
    time.sleep(1)
    t -= 1
  tts("Time up")
