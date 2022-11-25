## create a selenium webscraper to take a picture of a div

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

query = input("Ask question: ")

# set up chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

# set up webdriver
driver = webdriver.Chrome(r"C:\Users\Owner\Downloads\chromedriver_win32 (2)\chromedriver.exe",options=chrome_options)

# go to the page
driver.get("https://www.google.com/search?q=how+long+is+king+charles&oq=how+long+is+king+charles&aqs=chrome..69i57.4465j0j4&sourceid=chrome&ie=UTF-8")
time.sleep(15)
information = driver.find_element(By.XPATH("/html/body/div[8]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/span/span"))
information.screenshot()
information.save_screenshot("screenshot.png")

# taake a screenshot of the div


# close the browser
driver.quit()
