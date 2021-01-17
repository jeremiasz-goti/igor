import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

igor_input = input('> ')
options = Options()
options.headless = True
driver = webdriver.Chrome(r'C:/chromedriver.exe', options=options)
driver.get('https://www.naturalreaders.com/online/')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputDiv")))
text_input = driver.find_element(By.ID, 'inputDiv')
text_input.clear()
text_input.send_keys(igor_input)

driver.find_element(By.ID, 'playBtn').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="playBtn"]').click()
time.sleep(5)
driver.quit()