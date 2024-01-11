from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to the newly downloaded ChromeDriver executable
executable_path = 'C:\\Users\\vlogp\\Downloads\\chrome-win64\\chrome-win64'

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode (without GUI)

try:
    # Create the Chrome service
    chrome_service = Service(executable_path=executable_path)

    # Create the Chrome WebDriver using the service and options
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Replace 'your_website_url' with the URL of the website you want to automate
    website_url = 'https://chat.openai.com/?model=text-davinci-002-render-sha'

    # Navigate to the website
    driver.get(website_url)

    # Explicitly wait for the text area to be present
    text_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'prompt-textarea'))
    )

    # Clear any existing text in the text area (optional)
    text_area.clear()

    # Send a prompt or message to the text area
    text_area.send_keys("hello")

    # Submit the form (if needed)
    # text_area.submit()

    # Wait for a while to see the changes (you might need to adjust the duration)
    time.sleep(2)

    # Close the browser window
    driver.quit()

except Exception as e:
    print("Error:", e)
    raise
