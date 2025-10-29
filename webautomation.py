# from selenium import webdriver


# driver = webdriver.Chrome ()
# driver.get ("http://selenium.dev")


# driver.quit ()



# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


# chrome_option = Options ()
# chrome_option.add_experimental_option ("detach", True)

# driver = webdriver.Chrome (options = chrome_option)
# driver.get ("http://google.com")


# search = driver.find_element (By.TAG_NAME, "a")
# search = driver.find_element (By.ID, "title")
# search = driver.find_element (By.CLASS_NAME, "btn-blue")


# search_form.send_keys ('Alhazen Academy')


# search_form.submit ()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.keys import Keys

chrome_option = Options ()
chrome_option.add_experimental_option ("detach", True)
driver = webdriver.Chrome ()

driver.get ("http://www.google.com")
search = driver.find_element (By.NAME, "q")


search.send_keys ("Alhazen Academy" + Keys.ENTER)






























