#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__='JS'
__date__='2018.03.14'


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

# #豆瓣
# driver.get('https://www.douban.com/')

# elem_user = driver.find_element_by_id('form_email')
# elem_psw = driver.find_element_by_id('form_password')
#
# #可以自己修改登录名和账户密码
# elem_user.send_keys('295148018@qq.com')
# time.sleep(2)
# elem_psw.send_keys('********')
# time.sleep(2)
# 点击登录
# driver.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click()


# #知乎
# driver.get('https://www.zhihu.com/signup?next=%2F')
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
# elem_user = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
# elem_psw = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')
#
# elem_user.send_keys('18137980325')
# time.sleep(2)
# elem_psw.send_keys('********')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()


#百度贴吧

driver.get('https://tieba.baidu.com/')
driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

elem_user = wait.until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "#TANGRAM__PSP_10__userName")))
elem_psw = wait.until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "#TANGRAM__PSP_10__password")))
# elem_user = driver.find_element_by_xpath('input[@id="TANGRAM__PSP_10__userName"]')
# elem_psw = driver.find_element_by_xpath('input[@id="TANGRAM__PSP_10__password"]')

elem_user.send_keys('295148018@qq.com')
time.sleep(2)
elem_psw.send_keys('********')
time.sleep(2)

submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_10__submit'))).click()


