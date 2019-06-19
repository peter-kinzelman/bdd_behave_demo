from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.config import settings

class Page(object):
    driver = None

    def __init__(self):
      options = Options()

      for arg in settings['driver_arguments']:
        options.add_argument(arg)

      self.driver = webdriver.Chrome(executable_path="./bin/chromedriver", chrome_options=options)
