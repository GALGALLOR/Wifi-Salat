from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time
import datetime
def rebootfunc():
    PATH ="C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get('http://192.168.100.1')
    Advanced = driver.find_element_by_id('details-button')
    Advanced.click()

    time.sleep(3)
    Proceed_unsafe = driver.find_element_by_id('proceed-link')
    Proceed_unsafe.click()

    time.sleep(5)
    Account_name = driver.find_element_by_id('txt_Username')
    Account_name.click()
    Account_name.send_keys('root')

    Password = driver.find_element_by_id('txt_Password')
    Password.click()
    Password.send_keys('adminHW')
    Password.send_keys(Keys.RETURN)


    time.sleep(5)
    reboot = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/ul/li[1]/div')
    reboot.click()
    try:
        time.sleep(5)
        reboot = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/input[1]')
        reboot.click()
    except:
        time.sleep(3)
        pyautogui.click(318,314)
        time.sleep(4)
        pyautogui.click(631,201)
        pyautogui.click(1029,27)
        for num in range(1,100):
            time.sleep(1)
            print('------GO PRAY----')

def prayer_time():
    print('Scanning the time')
    prayer_times = ['5','6','13','16','18','19','20','21']
    prayer_minutes = ['0']
    while 1==1:
        hour_now = datetime.datetime.now().hour
        minute_now = datetime.datetime.now().minute
        second_now = datetime.datetime.now().second
        time.sleep(1)
        if str(hour_now) in prayer_times:
            if str(minute_now) in prayer_minutes:
                rebootfunc()
                print('----- I HOPE YOU HAVE ALREADY PRAYED-------')
        else:
            pass

prayer_time()



    
