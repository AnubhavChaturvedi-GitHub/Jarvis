from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pag

chrome_options = Options()
# chrome_options.add_argument('--headless')  # Add this line if you want to run Chrome in headless mode
chrome_options = Options()
# Specify the path to the ChromeDriver executable
chrome_driver_path = 'C:\\Users\\vlogp\\Desktop\\J.A.R.V.I.S\\Database\\chrome-headless-shell.exe'

# Set the executable path using chrome_options
chrome_options.binary_location = chrome_driver_path

# Initialize the Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

def login():
    # Getting the login element
    username = driver.find_element_by_id("login-email")

    # Sending the keys for username
    username.send_keys("your_username")  # Replace with your actual username

    # Getting the password element
    password = driver.find_element_by_id("login-password")

    # Sending the keys for password
    password.send_keys("your_password")  # Replace with your actual password

    # Getting the tag for the submit button
    driver.find_element_by_id("login-submit").click()

def goto_network():
    driver.find_element_by_id("mynetwork-tab-icon").click()

def send_requests():
    # Number of requests you want to send
    n = int(input("Number of requests: "))

    for i in range(n):
        # position(in px) of connection button
        pag.click(880, 770)
        time.sleep(2)  # Add a delay to give time for the connection dialog to appear

    print("Done !")

def main():
    # url of LinkedIn
    url = "http://linkedin.com/"

    # url of LinkedIn network page
    network_url = "http://linkedin.com/mynetwork/"

    # Open LinkedIn
    driver.get(url)

    # Perform login
    login()

    # Go to the network page
    driver.get(network_url)

    # Send connection requests
    send_requests()

    # Close the browser
    driver.quit()

# Driver's code
if __name__ == '__main__':
    main()
