from selenium import webdriver
from page import Page
import page

class AsteroidPage(Page):

  def eccentricity(self): return self.driver.find_element_by_xpath("//a[text()=\"e\"]/ancestor::td/following-sibling::td[1]")
  def epoch_osculation(self): return self.driver.find_element_by_xpath("//b[contains(text(),\"Orbital Elements at\")]")
  def semi_major_axis(self): return self.driver.find_element_by_xpath("//a[text()=\"a\"]/ancestor::td/following-sibling::td[1]")
