from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create a new instance of the Chrome driver with our profile
service = Service(executable_path="~/Library/Application Support/Google/Chrome/")

driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get('https://sellercentral.amazon.com/product-search?ref=xx_myiadprd_cont_myimain')



# Input username
textbox = driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
textbox.send_keys('dxgrandwayfitness@gmail.com')

# Input password
textbox = driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
textbox.send_keys('SquaredAsp7584')

# Click sign in
button = driver.find_element(By.CSS_SELECTOR, 'input#signInSubmit')
button.click()


# Keep the browser window open
input('Press ENTER to close the browser')

# Close the web driver and the browser window
driver.quit()