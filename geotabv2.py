import numpy as np
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import shutil
import os
import subprocess
import pandas as pd
import openpyxl

email = "it.sup@muneshwers.com"
password = "Mun3$hwers"
operator = input("windows or linux \n1 = Windows \n2 = linux \n :")

if operator == "1":
    driver = webdriver.Chrome("chromedriver.exe")
elif operator == "2":
    print("linux Selected")
    driver = webdriver.Chrome("chromedriver")
else:
    driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://my1013.geotab.com/#")

driver.find_element_by_id("userEmailId").send_keys(email)
driver.find_element_by_id("loginInputId").click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'userPasswordId')))
time.sleep(3)
driver.find_element_by_id("userPasswordId").send_keys(password)
driver.find_element_by_id("loginInputStep2Id").click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'navigationId')))
time.sleep(2)
driver.find_element_by_xpath('//*[@id="navigationId"]/ul/li[9]').click()
time.sleep(3)
driver.find_element_by_xpath(" // *[contains(text(), 'Report Set')]").click()
driver.find_element_by_xpath(" // *[contains(text(), 'Report Views')]").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_xpath(
    " // *[contains(text(), 'Advanced Trips Det')]").click()
time.sleep(2)
driver.find_element_by_id("customReport_viewReport").click()
time.sleep(2)
driver.find_element_by_id("leaveWithoutSaving").click()
time.sleep(20)
driver.find_element_by_id('menuToggle').click()
time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="tripsHistory_reports"]/button').click()
time.sleep(2)
driver.find_element_by_id(
    "template_ReportTemplateAdvancedTripsDetailId").click()
time.sleep(20)
if operator == "2":
    subprocess.call(['sh', './move.sh'])
elif operator == "1":
    print("placeholder")
    # subrocess.call(['ps'] '')
    subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
                   r'C:\Users\%username%\Documents\Geotab\move.ps1'])


file_loc = "Raw.xlsx"
df = pdf = pd.read_excel(file_loc, usecols="A,R")

print(df)
