from selenium import webdriver
from data.config import settings
import time
import requests
from page.yahoo_page import YahooPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Stocks():
  instance = None
  page = None

  @classmethod
  def get_instance(cls):
    if cls.instance is None:
      cls.instance = Stocks()
    cls.instance.page = YahooPage()
    return cls.instance

  def get_yahoo_stocks(self):
    self.page.driver.get('https://finance.yahoo.com/lookup')

  def get_company_page(self, data, errors):
    self.page.searchBox().send_keys(data[0]['symbol'])
    self.page.searchButton().click()
    counter = 0

  def verify_ui_data(self, data, errors):
    amounts = []
    counter = 0

    for x in range(5):
      time.sleep(1)
      stockAmmount = WebDriverWait(self.page.driver, 20).until(
      EC.element_to_be_clickable((By.XPATH, "//*[@id='quote-header-info']/div[3]/div[1]/div/span[1]")))
      amounts.append(float(stockAmmount.text[:4]))
    
    if float(str(data[0]['price'])[:4]) not in amounts: errors.append("The Yahoo web page has different data then the API")

yahoo = Stocks.get_instance()
