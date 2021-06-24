from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

def main():
    url = """https://www.facebook.com/KAWAIKANYUDROP/posts/4589965157722109""" #replace this link
    facebookLogin="" # fill in login info here
    facebookPass="" #fill in password here
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    driver.find_element_by_id('email').send_keys(facebookLogin)
    driver.find_element_by_id('pass').send_keys(facebookPass)
    driver.find_element_by_id('loginbutton').click()
    block=pyautogui.locateOnScreen('blockBTN.JPG',confidence=0.6)
    while block is None:
        block=pyautogui.locateOnScreen('blockBTN.JPG',confidence=0.6)
    time.sleep(0.5)
    pyautogui.click((block[0]+10),block[1]+10)
    print("slept")
    time.sleep(0.1)
    for i in range(30):
        driver.find_element_by_xpath('//body').send_keys(Keys.DOWN)
        po = pyautogui.locateOnScreen('likeBTN.JPG', confidence=0.6)
        if po is not None:
            po = pyautogui.locateOnScreen('likeBTN.JPG', confidence=0.6)
            pyautogui.moveTo(int(po[0]+10),int(po[1]+10))
            time.sleep(1)
            for i in range(10):
                angry = pyautogui.locateOnScreen('angryBTN.JPG', confidence=0.7)
                if (angry is not None):
                    pyautogui.click(x=int(angry[0]+10),y=int(angry[1]+10))
                    break
            break
    print(po)
    time.sleep(10)

if __name__ == "__main__":
    main()