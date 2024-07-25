# Install selenium using pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import Keys because Keys are used to send special keys like ENTER, F1, ALT etc.
from selenium.webdriver.common.keys import Keys
import time

# If your chrome close instantly then use below code --------------------->

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# ------------------------------------------------------------------------->

# Create a driver object
driver = webdriver.Chrome(options=options, service=Service("C:/Users/dhanr/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# Open the website
driver.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Chennai')
time.sleep(6)

# # driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div[4]/div[3]/div[3]/div[4]/a').click()
old_height = driver.execute_script('return document.body.scrollHeight')
counter = 1
while counter < 80:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height==old_height:
        break

    old_height = new_height


# # Get the html of the page
html = driver.page_source

# # Save the html in a file
with open('chennai.html','w',encoding='utf-8') as f:
    f.write(html)