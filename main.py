import sys
import datetime
import selenium
import requests
import pdb
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

parser = OptionParser()
now = datetime.datetime.now()
pr_query_url = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the GitHub pull request query URL: ')

options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=options)
driver.get(pr_query_url)
driver.maximize_window()
# pdb.set_trace()

driver.set_window_size(driver.get_window_size()['width'], driver.get_window_size()['height'])
pr= open("pull_requests.csv","a")

elem_size=len(driver.find_elements_by_css_selector(".pagination > a[aria-label]"))
count = int(driver.find_element_by_xpath("(//*[@class='pagination']//a)["+str(elem_size)+"]").text)

for i in range(count):
    elems = driver.find_elements_by_css_selector("[data-hovercard-type='pull_request']")
    for x in elems:
        pr.write(x.text.encode('utf-8').strip()+"\n")

    pr.write("==========Page "+str(i+1)+"=========="+"\n")
    
    if i != count-1:
        driver.find_element_by_xpath("(//*[@class='next_page'])[1]").click()
        t.sleep(5)

pr.close()
driver.close()
driver.quit()