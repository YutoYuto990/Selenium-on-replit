from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")
driver.maximize_window()
driver.find_element(By.NAME,"word").send_keys("keys")
driver.find_element(By.XPATH,"//form/input").click()
el=driver.find_elements(By.XPATH,"//p/a")
#.........