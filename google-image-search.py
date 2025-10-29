from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.keys import Keys

chrome_option = Options ()
chrome_option.add_experimental_option ("detach", True)
driver = webdriver.Chrome ()

driver.get ("http://images.google.com")
search = driver.find_element (By.NAME, "q")


search.send_keys ("logo python" + Keys.ENTER)
search.submit ()
