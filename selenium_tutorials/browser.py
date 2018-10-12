from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://imdb.com'

driver.get(url)

current_url = driver.current_url

print(current_url)

driver.quit()
