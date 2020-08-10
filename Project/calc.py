from SenseCells.tts import tts


def add(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('add')
	words_of_message.remove('with')
	s = ' '.join(words_of_message)
	x, y = s.split()
	x = float(x)
	y = float(y)
	z = x + y
	z = str(z)
	tts(z)

def sub(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('subtract')
	words_of_message.remove('from')
	s = ' '.join(words_of_message)
	x, y = s.split()
	x = float(x)
	y = float(y)
	z = y - x
	z = str(z)
	tts(z)

def multi(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('multiply')
	words_of_message.remove('with')
	s = ' '.join(words_of_message)
	x, y = s.split()
	x = float(x)
	y = float(y)
	z = x*y
	z = str(z)
	tts(z)

def div(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('divide')
	words_of_message.remove('with')
	s = ' '.join(words_of_message)
	x, y = s.split()
	x = float(x)
	y = float(y)
	z = x/y
	z = str(z)
	tts(z)
