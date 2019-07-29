from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/Users/apple/Downloads/chromedriver')
driver.get('https://www.linkedin.com/login')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.send_keys('allenjohnbinu@gmail.com')
password.send_keys('Appu99$$')
password.send_keys(Keys.RETURN)


driver.get('https://www.linkedin.com/in/akshanth-r-b77141170/')
more = driver.find_element_by_id('ember58').click()
pdf = driver.find_element_by_id('ember67').click()