'''
PROJECT : AUTOMATED DOWNLOAD OF LINKEDLIN CONNECTIONS OF A GIVEN PROFILE
importing the required packages for the project
'''

import shutil
import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
creating the excel sheet for storing the information about the connections of a given profile
'''

cf = open('link1_ex.csv', 'w')
cw = csv.writer(cf)
cw.writerow(['NAME', 'POSITION', 'LINK'])
'''
collection of the webdriver using the specified path
going to linkedin login page
entering the username and password
going to connections page and getting the raw data
'''

driver = webdriver.Chrome('/Users/apple/Downloads/chromedriver')
driver.get('https://www.linkedin.com/login')
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys('allenjohnbinu@gmail.com')
password.send_keys('Appu99$$')
password.send_keys(Keys.RETURN)
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
mylist = driver.find_elements_by_class_name('mn-connection-card')
'''
creating linkl for the collection of links of the connections of the given profile
and names for the collection of names of the connections of the given profile
'''

linkl = []
names = []
'''
traversal through the raw data collected, for the name, position and their respective links
information are written to the excel sheet
'''

for profile in mylist:
  details = profile.text.split('\n')
  if details[0] == 'Status is reachable':
    del details[0]
  profile_name = details[1]
  profile_slug = details[3]
  url_element = profile.find_element_by_tag_name('a')
  profile_url = url_element.get_attribute('href')
  linkl.append(profile_url)
  names.append(profile_name)

  cw.writerow([profile_name, profile_slug, profile_url])

i = 0
'''
traversal through the linkl for the downloading of the specified connection link
giving a delay for downloading the connection's resume
moving the downloaded resume to a folder called 'LINK'
renaming it with connection's name
'''
for url in linkl:
  driver.get(url)
  more = driver.find_element_by_id('ember58').click()
  pdf = driver.find_element_by_id('ember67').click()

  time.sleep(10)

  src = '/Users/apple/Downloads/Profile.pdf'
  des = '/Users/apple/LINK'
  shutil.move(src, des)

  os.rename('/Users/apple/LINK/Profile.pdf', '/Users/apple/LINK/'+names[i]+'.pdf')
  i = i + 1

cf.close()