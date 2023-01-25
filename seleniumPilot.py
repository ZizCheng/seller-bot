from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as webdriver

# Create a new instance of the Chrome driver with the --remote-debugging-port option
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get("https://www.google.com/")

# Find the textbox element by its id
textbox = driver.find_element_by_id("input.gLFyf")

# Input text into the textbox
textbox.send_keys("Hello World!")