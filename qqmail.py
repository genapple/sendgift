#!/usr/bin/python
#-*- coding:UTF-8 -*-
import  time
from selenium import  webdriver
url="http://www.baidu.com"
url1="https://mail.qq.com/"
driver = webdriver.Chrome()
driver.get(url)
#button1=driver.find_element_by_xpath('//*[@id="switcher_plogin"]')
#button1=driver.find_element_by_id("switcher_plogin")
button1=driver.find_element_by_xpath('//*[@id="kw"]')
button1.send_keys("test")
#implicity_wait(10)
#driver.implicitly_wait(10)
#button1.click()
print 'I have been  click'
