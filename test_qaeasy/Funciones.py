import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")
global driver
