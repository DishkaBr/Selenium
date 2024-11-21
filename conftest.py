
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--lang=en-US")
driver = webdriver.Chrome(options=options)

base_url = "https://rickandmortyapi.com/api"

file_path = "/Users/dianabrook/PycharmProjects/pythonProjectSelenium/characters_introduction.txt"

google_url = 'https://www.google.com/'

