#! /usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

print('Paste linkedin URL while clicked on the job you just applied to')
url = input()

browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
time.sleep(2)


#first sign in click on linkedin
signInBtn1 = browser.find_element(By.XPATH, '/html/body/div[3]/a[1]')
signInBtn1.click()
time.sleep(2)

#second sign in click on linkedin
cwd = os.getcwd()
load_dotenv(cwd+'/secrets.env')
username = str(os.getenv('USERNME'))
password = str(os.getenv('PASSWORD'))
time.sleep(2)
usernameInput = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
passwordInput = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
signInBtn2 = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')

usernameInput.send_keys(username)
passwordInput.send_keys(password)
signInBtn2.click()
time.sleep(3)

try:
    name = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a/h2')
except: 
    print('name failed')
try:
    company = browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a' )
except: 
    print('company failed')
try:
    location = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[2]')
except: 
    print('location failed')
try:
    postingLink = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a')
except: 
    print('link failed')
postingLink = postingLink.get_attribute('href')


print(name.text)
print(company.text)
print(location.text)
print(postingLink)
