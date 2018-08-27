from selenium import webdriver

#driver = webdriver.Chrome("D:/AutoConf/bin/chromedriver.exe")  #错误的路径 使用正斜杠
driver = webdriver.Chrome("D:/Program Files (x86)/Google/Chrome/Application/chrome.exe") #正确的路径 使用反斜杠

driver.get("http://www.baidu.com")