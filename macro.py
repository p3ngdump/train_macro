#-*- coding: utf-8 -*-

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("D:\\chromedriver.exe")

driver.implicitly_wait(3)

driver.get("http://www.letskorail.com/korail/com/login.do")

driver.find_element_by_id("txtMember").send_keys("ID")
driver.find_element_by_id("txtPwd").send_keys("PW")

driver.find_element_by_xpath("//*[@id=\"loginDisplay1\"]/ul/li[3]/a/img").click()



start_station = "출발역"
end_station = "도착역"

driver.get("http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do")

# start station
driver.find_element_by_name("txtGoStart").clear()
driver.find_element_by_name("txtGoStart").send_keys(start_station.decode('utf-8'))

# end station
driver.find_element_by_name("txtGoEnd").clear()
driver.find_element_by_name("txtGoEnd").send_keys(end_station.decode('utf-8'))

# month
select = Select(driver.find_element_by_id("s_month"))
select.select_by_value("11") # select month

# date
select2 = Select(driver.find_element_by_id("s_day"))
select2.select_by_value("24") # select date

# time
select3 = Select(driver.find_element_by_id("s_hour"))
select3.select_by_value("00") # select time

driver.find_element_by_xpath("//*[@id=\"center\"]/form/div/p/a/img").click()

# book loop
while(1):
	try:
		value = driver.find_element_by_xpath("//*[@id=\"tableResult\"]/tbody/tr[2]/td[6]/a[1]/img")
		if value:
			value.click()
			break
	except:
		driver.find_element_by_xpath("//*[@id=\"center\"]/div[3]/p/a/img").click()
