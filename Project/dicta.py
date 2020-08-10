from PyDictionary import PyDictionary
from SenseCells.tts import tts
import re
from string import punctuation

def PyD(speech_text):
	
	words_of_message = speech_text.split()
	words_of_message.remove('meaning')
	words_of_message.remove('of')
        cleaned_message = ' '.join(words_of_message)

	try:		
		dictionary = PyDictionary()
		s = dictionary.meaning(cleaned_message)
		def strip_punctuation(s):
        		return ''.join(c for c in s if c not in punctuation)
		regex = re.compile(".*?\((.*?)\)")
		result = re.findall(regex, mystring)
		for char in string.punctuation:
			s = s.replace(char, ' ')
			s = re.sub(r'[^\w]', ' ', s)
		regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
		m = regEx.match(s)
		while m:
			s = m.group(1) + m.group(2)
			m = regEx.match(s)

		s = s.replace("'","")
		a = strip_punctuation(s)
		print(a)
		tts(s)
	except:
		print("Can you please be more specific? You may choose something from the following.; {0}")
		
