from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
xpath_id='//*[@id="id"]'
xpath_pw='//*[@id="pw"]'
driver = webdriver.Chrome()
options=Options()
driver.set_window_size(1800,1000)
url = 'https://cyber.inhatc.ac.kr'
driver.get(url)
tabs=driver.window_handles
print(tabs)

driver.switch_to.window(tabs[1])
driver.close()
driver.switch_to.window(tabs[2])
driver.close()
driver.switch_to.window(tabs[0])
iframe=driver.find_element(By.NAME,'main')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,xpath_id).send_keys('202245087')
driver.find_element(By.XPATH,xpath_pw).send_keys('0725!2022')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/p/a').send_keys(Keys.ENTER)
driver.execute_script("arguments[0].style.display = 'none';",driver.find_element(By.ID,'imagePop'))
driver.find_element(By.ID,'#').click()
driver.find_element(By.XPATH,'//*[@id="#"]/fieldset/div/div/ul/li[11]').click()
while(1):
    if(driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div/ul[2]/li[2]/a[3]').text=='학습 하기'):
        driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div/ul[2]/li[2]/a[3]').click()
        break
    elif(driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[2]/div/ul[2]/li[2]/a[3]').text=='학습 하기'):
        driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[2]/div/ul[2]/li[2]/a[3]').click()
        break
    elif(driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[3]/div/ul[2]/li[2]/a[3]').text=='학습 하기'):
        driver.find_element(By.XPATH,'//*[@id="listBox"]/table/tbody/tr[1]/td[3]/div/ul[2]/li[2]/a[3]').click()
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="listBox"]/table/thead/tr/th[4]/p/a/img').click()
