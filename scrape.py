from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


question = input("Question: ")
query = question.replace(' ','+')
print(query)



driver = webdriver.Chrome(r'C:\Users\Joe\Downloads\chromedriver.exe')
driver.get('https://www.google.com/search?q='+query)
time.sleep(1.5)
box = driver.find_element("xpath",'/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').click()
content = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div').get_attribute("textContent")
print(content)