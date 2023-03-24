#! /usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os
import openpyxl
from openpyxl import load_workbook

print('Paste linkedin URL while clicked on the job you just applied to')
url = input()

# # #runs selenium browser invisibly so you can just operate from CLI
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')


print('Loading Linkedin...')
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.maximize_window()
time.sleep(2)

print('Navigating to sign in page...')
#first sign in click on linkedin
signInBtn1 = browser.find_element(By.XPATH, '/html/body/div[3]/a[1]')
signInBtn1.click()
time.sleep(2)

print('Inputting credentials...')
#second sign in click on linkedin
cwd = os.getcwd()
load_dotenv(cwd+'/secrets.env')
username = str(os.getenv('USERNME'))
password = str(os.getenv('PASSWORD'))
usernameInput = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
passwordInput = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
signInBtn2 = browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')

#TODO: Find a way to do this async based on page load, not just waiting arbitrary amount of time

usernameInput.send_keys(username)
passwordInput.send_keys(password)
signInBtn2.click()
time.sleep(3)

#TODO: add date, easyapply, etc

print('Success! Saving job info to local variables')
try:
    name = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a/h2')
    #print(name.text)
except: 
    print('name failed')
try:
    company = browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]/a' )
    #print(company.text)
except: 
    print('company failed')
try:
    location = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[2]')
    #print(location.text)
except: 
    print('location failed')
try:
    postingLink = browser.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    postingLink = postingLink.get_attribute('href')
    #print(postingLink)
except: 
    print('link failed')

#postingLink = postingLink.get_attribute('href')
# print(name.text)
# print(company.text)
# print(location.text)
# print(postingLink)
#browser.quit()

#create excel if it doesn't exists
if not (os.path.isfile(cwd+'/Job_Search_Log.xlsx')):
    print('Creating workbook...')
    wb = openpyxl.Workbook()
    wb_name = 'Job_Search_Log.xlsx'
    ws = wb.active
    ws.title ='Job_Search_Log'
    ws['A1'] = 'Name'
    ws['B1'] = 'Company'
    ws['C1'] = 'Location'
    ws['D1'] = 'Link'
    wb.save(cwd+'/Job_Search_Log.xlsx')
    wb.close()

#Write new info to workbook
editBook = load_workbook(filename=cwd+'/Job_Search_Log.xlsx')
ws = editBook.active
rowToWrite = str(ws.max_row + 1)
print('Writing to row ' + rowToWrite + '...')
print(ws['A'+rowToWrite])
#TODO: if one of these was not available, need a try, except or something to prevent program crashing
ws['A' + rowToWrite] = str(name.text)
ws['B' + rowToWrite] = str(company.text)
ws['C' + rowToWrite] = str(location.text)
ws['D' + rowToWrite] = str(postingLink)
print('cwd')
print(cwd+'/Job_Search_Log.xlsx')
editBook.save(cwd+'/Job_Search_Log.xlsx')
#TODO: tell what you are writing to workbook, ie writing [name,company]
print('wb saved!')
# editBook.close()
    
