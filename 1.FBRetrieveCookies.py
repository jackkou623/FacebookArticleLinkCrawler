# coding=utf-8
import time                  
import os    
import codecs  
import json
from selenium import webdriver        
from selenium.webdriver.common.keys import Keys        
from pathlib import Path

#Global variables:
Cloc = Path(os.path.abspath("")) #Current Location
Coloc = Cloc / "FBCookies.txt" #Cookies location
driver=webdriver.Chrome('chromedriver.exe')   

# Function 1: Login FB
def Login(username,password):
    try:
       driver.get("https://www.facebook.com/")
       
       time.sleep(2)
       
       driver.find_element_by_id("email").send_keys(username)
       driver.find_element_by_id("pass").send_keys(password)
       driver.find_element_by_xpath("//*[@value='Log In']").click()
       time.sleep(2)
       
       #Function 2: get Cookies
       print ("Cookies are retrieving")
       time.sleep(10)
       cookies = driver.get_cookies()
       print (cookies)
       f = open(Coloc, 'w') 
       f.write(json.dumps(cookies))  #json.dumps must be included
       f.close()
       
    except:      
        print("Error")
    finally:    
        print('End LoginFaceBookSuccessfully!\n\n')
       
Login("login email","login pw") #type your login account and pw here
driver.quit()