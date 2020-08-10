from selenium import webdriver

from SenseCells.tts import tts

def connect_to_proxy(proxy_username, proxy_password):
	tts("Connecting to proxy server...")
	browser = webdriver.Firefox()
	browser.get('https://www.gmail.com')

	id_number = browser.find_element_by_name('email')
	password = browser.find_element_by_name('password')

	id_number.send_keys(proxy_username)
	password.send_keys(proxy_password)

	browser.find_element_by_name('btnSubmit').click()

