from selenium import webdriver
from page import Page
import page

class YahooPage(Page):

    def searchBox(self): return self.driver.find_element_by_id('yfin-usr-qry')
    def searchButton(self): return self.driver.find_element_by_id('search-buttons')
