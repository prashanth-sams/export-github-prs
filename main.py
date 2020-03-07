import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=options)
driver.get("")
elem_size=len(driver.find_elements_by_css_selector(".pagination > a[aria-label]"))
count = int(driver.find_element_by_xpath("(//*[@class='pagination']//a)["+str(elem_size)+"]").text)
print(count)

with open('pull_requests.csv','a') as pr:
    value = 0
    while value < count:
        elems = driver.find_elements_by_css_selector("[data-hovercard-type='pull_request']")
        for x in elems:
            pr.write(x.text+"\n")

        t.sleep(2)
        if value != count-1:
            driver.find_element_by_xpath("(//*[@class='next_page'])[1]").click()
            value += 1

driver.close()
driver.quit()