#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:49:13 2018

@author: laulau
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#INIT driver
driver = webdriver.Firefox()
driver.get("https://framalistes.org/sympa/loginrequest")


#login to framalistes
email = driver.find_element_by_name('email')
passwd = driver.find_element_by_name('passwd')
email.send_keys("laurent.maingault@yahoo.fr")
passwd.send_keys("Laurent8")
login = driver.find_element_by_name('action_login')
login.click()

input()

#loop
driver.get("https://framalistes.org/sympa/review/parents-buffon")

email_list = ["ecole-buffon@yahoo.com","bibizzzmaing@gmail.com"]

for email_add in email_list:
    new_email_addr = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,'email_search')))
    new_email_addr = driver.find_element_by_id('email_search')
    new_email_addr.send_keys(email_add)
    add = driver.find_element_by_name('action_add')
    add.click()
    confirm = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'response_action_confirm')))
    confirm.click()


driver.quit()