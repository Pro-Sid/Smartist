from GreyMatter import tell_time, general_conversations, weather, define_subject, business_news_reader, open_firefox, sleep, play_music, notes,calc, timer, dicta

def brain(name, speech_text, city_name, city_code, proxy_username, proxy_password, music_path):
    def check_message(check):
        """
        This function checks if the items in the list (specified in argument) are present in the user's input speech.
        """

        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(['who','are', 'you']):
        general_conversations.who_are_you()

    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversations.how_am_i()

    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()

    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()

    elif check_message(['time']) or check_message(['tell','me','time']) or check_message(['whats','the','time']):
        tell_time.what_is_time()

    elif check_message(['how','weather']) or check_message(['hows','weather']) or check_message(['whats','weather']):
	weather.weather(city_name, city_code)

    elif check_message(['define']) or check_message(['what','is']):
	define_subject.define_subject(speech_text )

    elif check_message(['business','news']):
	business_news_reader.news_reader()

    elif check_message(['open','firefox']):
	open_firefox.open_firefox()

    elif check_message(['sleep']) or check_message(['by']) or check_message(['bye']) or check_message(['good','night']):
	sleep.go_to_sleep()

    elif check_message(['play','music']) or check_message(['music']) or check_message(['song']):
	play_music.play_random(music_path)

    elif check_message(['play']):
	play_music.play_specific_music(speech_text, music_path)

    elif check_message(['party', 'time']) or check_message(['party', 'mix']):
        play_music.play_shuffle(music_path)

    elif check_message(['note']):
	notes.note_something(speech_text)

    elif check_message(['all', 'notes']) or check_message(['notes']):
	notes.show_all_notes()

    elif check_message(['add']):
	calc.add(speech_text)

    elif check_message(['subtract']):
	calc.sub(speech_text)

    elif check_message(['multiply']):
	calc.multi(speech_text)

    elif check_message(['divide']):
	calc.div(speech_text)

    elif check_message(['set','timer']):
	timer.countdown(speech_text)

    elif check_message(['meaning','of']):
	dicta.PyD(speech_text)

    else:
	general_conversations.undefined()
