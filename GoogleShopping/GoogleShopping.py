from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service = ChromeService(executable_path="../drivers/chromedriver")  # relative to this script
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com.au")
driver.find_element(by=By.CSS_SELECTOR, value="[title='Search']").send_keys("xiaomi air purifier")
driver.find_element(by=By.XPATH, value="//center[not(preceding-sibling::style)]/input[@value='Google Search']").click()

driver.close()