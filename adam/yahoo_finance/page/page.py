from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Page(object):
    driver = None

    def __init__(self):
      options = Options()
      options.add_argument('--headless')

      self.driver = webdriver.Chrome(executable_path="./bin/chromedriver", chrome_options=options)


"""

see adam/nasa_asteroids/pages directory for how we'll be setting up Page Objects

"""