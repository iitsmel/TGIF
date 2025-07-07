#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# https://www.selenium.dev/documentation/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://unknown/reset-password')

current_element = browser.find_element(By.NAME, 'account')
account = "username"
for character in account:
    current_element.send_keys(character)
    time.sleep(0.1)

current_element = browser.find_element(By.NAME, 'password') 
password = "password"
for character in password:
    current_element.send_keys(character)
    time.sleep(0.1)


current_element = browser.find_element(By.NAME, 'checkPassword')
current_element.send_keys('password' + Keys.RETURN)