#from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
#import time

#options = Options()
#options.headless = True

# Change the URL to your web app (localhost or your deployed link)
#url = 'http://localhost:3000'

# Start Firefox in headless mode
#driver = webdriver.Firefox(options=options)
#driver.get(url)

#print("Opened", url)
#time.sleep(5)
#print("Closing browser now.")

#driver.quit()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
# options.headless = True  # <-- Make sure this line is removed or commented out

url = 'http://localhost:3000'

driver = webdriver.Firefox(options=options)
driver.get(url)

print("Opened", url)
time.sleep(5)
print("Closing browser now.")

driver.quit()

