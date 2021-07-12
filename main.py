

from logging import BASIC_FORMAT
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SLEEP_TIME = 1.5
FB_EMAIL = "INPUT EMAIL HERE"
FB_PASSWORD = "INPUT PASSWORD HERE"

URL = "https://tinder.com/"

# options = webdriver.ChromeOptions() 
# options.add_argument("user-data-dir=C:\\Users\\janti\\AppData\\Local\\Google\\Chrome\\User Data")
# w = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", chrome_options=options)
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
time.sleep(2)
driver.get(URL)
driver.maximize_window()
time.sleep(5)

'''Tinder Login'''
driver.get(URL)
driver.maximize_window()
time.sleep(2)
tinder_login = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
tinder_login.click()
time.sleep(SLEEP_TIME)

'''Facebook Login'''
fb_login = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
fb_email = driver.find_element_by_id("email")
fb_email.send_keys(FB_EMAIL)
fb_pass = driver.find_element_by_id("pass")
fb_pass.send_keys(FB_PASSWORD)
time.sleep(SLEEP_TIME)
fb_pass.send_keys(Keys.ENTER)

'''Tinder swipe'''
driver.switch_to.window(base_window)
time.sleep(8)
'''Allow Location'''
allow_location_button = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
'''Disallow notification'''
notifications_button = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()
'''Allow cookies'''
cookies = driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[2]/div/div/div[1]/button')
cookies.click()


time.sleep(3)
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(2)

    try:
        like_button = driver.find_element_by_xpath(
            '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span')
        like_button.click()
    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except:
        try:
            like_button_post = driver.find_element_by_xpath(
                '//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
            like_button_post.click()
        except:
            try:
                match_popup = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[4]/button')
                match_popup.click()

            #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
            except:
                time.sleep(2)
