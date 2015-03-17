#!/usr/bin/env python3
import os
import unittest
from selenium import webdriver
os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.45.0.jar"

class VistorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(10)
	def tearDown(self):
		self.browser.quit()
	def test_do_something(self):
		self.assertIn('aa','aa')

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://52.11.139.225:8000')
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finished the Test')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
