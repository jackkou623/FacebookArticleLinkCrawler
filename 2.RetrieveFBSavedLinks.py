# coding=utf-8
from xml.dom import minidom
import time            
import re        
import os 
import sys  
import codecs  
import shutil
import urllib
import json
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys   
import selenium.webdriver.support.ui as ui        
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path

#Global variables:
Cloc = Path(os.path.abspath("")) #Current Location
Coloc = Cloc / "FBCookies.txt" #Cookies location
Lloc = Cloc / "Links.txt"
links = []

#Disable Chrome notification alerts
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#Input cookies
driver.get("https://www.facebook.com/")
driver.maximize_window() 
time.sleep(5)
f = open(Coloc)
cookie = f.read()
cookie = json.loads(cookie)
for c in cookie:
        if 'expiry' in c:
                del c['expiry'] #For Chrome version above 76.x
                driver.add_cookie(c)
        else:
                driver.add_cookie(c)
driver.get("https://www.facebook.com/")
print("Cookies are successfully input-ed.")

#Retrieve all links
driver.get("https://www.facebook.com/saved/all") #Put your FB saved link here e.g. https://www.facebook.com/saved/all

for a in range(50): #Whatever number, just scroll to the bottom of the page, default is 50
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)

x = driver.find_elements_by_xpath("//*[@class='_24-s']")
print(len(x))
for a in range(0,len(x),2):
        links.append(x[a].get_attribute('href'))
f = open(Lloc, 'w') 
f.write(str(links))
f.close()