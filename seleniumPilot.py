import env
import undetected_chromedriver as webdriver
import time



options = webdriver.ChromeOptions()
profile = dir
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options, use_subprocess=True)
driver.get("https://amazon.com")

time.sleep(1000000)