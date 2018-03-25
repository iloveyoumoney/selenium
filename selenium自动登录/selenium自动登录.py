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
driver.set_window_position(x=50, y=60)
driver.set_window_size(width=1366, height=700)
wait = WebDriverWait(driver,10)


# 百度贴吧
def baidu_tieba():

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
      elem_psw.send_keys('*******')
      time.sleep(2)
      wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#TANGRAM__PSP_10__submit'))).click()
      time.sleep(10)
      driver.close()  # 关闭浏览器

#豆瓣
def douban():

      driver.get('https://www.douban.com/')

      elem_user = driver.find_element_by_id('form_email')
      elem_psw = driver.find_element_by_id('form_password')

      #可以自己修改登录名和账户密码
      elem_user.send_keys('295148018@qq.com')
      time.sleep(2)
      elem_psw.send_keys('*******')
      time.sleep(2)
      点击登录
      driver.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click()



# #知乎
def zhihu():

      driver.get('https://www.zhihu.com/signup?next=%2F')
      driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
      elem_user = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input')
      elem_psw = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input')

      elem_user.send_keys('18137980325')
      time.sleep(2)
      elem_psw.send_keys('********')
      time.sleep(2)
      driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()


      # driver.get('https://www.zhihu.com/topic/19563245/followers')  # 跳转到清华大学话题
      # sleep(2)
      # # 点击更多按钮进行加载
      # driver.find_element_by_id('zh-load-more').click()
      # print('加载一次')
      # jiazai = 0
      # try:
      #       while (driver.find_element_by_id('zh-load-more') and jiazai < 100):
      #             print('点击加载:' + str(jiazai))
      #             jiazai = jiazai + 1
      #             driver.find_element_by_id('zh-load-more').click()
      # except:
      #       print('没有更多了')
      #
      # info = driver.find_elements_by_class_name('zm-list-avatar-medium')
      # f = open('user.txt', 'w')
      # for item in info:
      #       link = item.get_attribute('href')  # 保存用户的个人链接
      #       f.write(link + '\n')
      #
      #       '''
      #       pa = re.compile('people/(\w*)$')
      #       try:
      #           userId=pa.findall(str(link))[0]
      #       except:
      #           userId='none'
      #       img_url=item.find_element_by_css_selector('img').get_attribute('src')
      #       if img_url!=None: #保存头像
      #           f=open(os.path.join('./img',userId+'.jpg'),'wb')
      #           f.write(requests.get(img_url).content)
      #           f.close()
      #       '''
      #       # driver.close()  #关闭浏览器

if __name__=='__main__':
      baidu_tieba()
      # zhihu()
      # douban()
