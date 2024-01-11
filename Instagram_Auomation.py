# importing module
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# enter receiver user name
user = ['User_name', 'User_name ']
message_ = ("final test")


class bot:
	def __init__(self, username, password, user, message):
		self.username = username
		self.password = password
		self.user = user
		self.message = message
		self.base_url = 'https://www.instagram.com/'
		self.bot = driver
		self.login()

	def login(self):
		self.bot.get(self.base_url)

		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)
		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)
		enter_password.send_keys(Keys.RETURN)
		time.sleep(5)

		# first pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
		time.sleep(5)

		# 2nd pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		time.sleep(5)

		# direct button
		self.bot.find_element(By.XPATH,
							'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div/a').click()
		time.sleep(3)

		# clicks on pencil icon
		self.bot.find_element(By.XPATH,
							'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
		time.sleep(2)
		for i in user:

			# enter the username
			self.bot.find_element(By.XPATH,
								'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
			time.sleep(3)

			# click on the username
			self.bot.find_element(By.XPATH,
								'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
			time.sleep(4)

			# next button
			self.bot.find_element(By.XPATH,
								'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button').click()
			time.sleep(4)

			# click on message area
			send = self.bot.find_element(By.XPATH,
										'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

			# types message
			send.send_keys(self.message)
			time.sleep(1)

			# send message
			send.send_keys(Keys.RETURN)
			time.sleep(2)

			# clicks on direct option or pencil icon
			self.bot.find_element(By.XPATH,
								'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[1]/div/div[3]/button').click()
			time.sleep(4)


def init():
	bot('username', 'password', user, message_)

	# when our program ends it will show "done".
	input("DONE")


# calling the function
init()
