from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

msc = input('Enter a music:')

nav = webdriver.Chrome() #webdriver v99
nav.maximize_window()
nav.get('https://www.youtube.com/results?search_query={}'.format(msc))

wait = WebDriverWait(nav, 7)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
nav.find_element_by_id("search-icon-legacy").click()
wait.until(visible((By.ID, "video-title")))
nav.find_element_by_id("video-title").click()
time.sleep(7)
wait.until(visible((By.ID, 'skip-button:p')))
nav.find_element_by_id('skip-button:p').click()
nav.find_elements_by_xpath('//*[@id="movie_player"]/div[34]/div[2]/div[1]/a[2]').get_attribute('data-duration')
tempo = 'data-duration'
def countdown(tempo):
    while tempo:
        m, s = divmod(tempo, 'data-duration')
        nav.quit()



