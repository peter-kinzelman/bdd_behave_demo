from selenium import webdriver
from data.config import settings
import time
import requests
from pages.asteroid_page import AsteroidPage


class Asteroids():
  instance = None
  page = None

  @classmethod
  def get_instance(cls):
    if cls.instance is None:
      cls.instance = Asteroids()
    cls.instance.page = AsteroidPage()
    return cls.instance

  def verify_asteroid(self, data, errors):
    counter = 0
      
    for f in data:
      if counter < 5:
        self.page.driver.get(f['nasa_jpl_url'].replace("http://", "https://"))
        response = requests.request("GET", f['links']['self'])
        asteroidData = response.json()

        if self.page.eccentricity().text != asteroidData['orbital_data']['eccentricity']: errors.append('The eccentricity data is incorrect at index ' + str(counter) )
        if asteroidData['orbital_data']['epoch_osculation'] not in self.page.epoch_osculation().text : errors.append('The epoch osculation data is incorrect at index ' + str(counter) )
        if asteroidData['orbital_data']['semi_major_axis'] != self.page.semi_major_axis().text : errors.append('The semi major axis is incorrect at index ' + str(counter) )
        counter += 1

asteroid = Asteroids.get_instance()
