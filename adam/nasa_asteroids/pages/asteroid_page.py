# class AsteroidPage(Page):
#
#   def eccentricity(self): return self.driver.find_element_by_xpath("//a[text()=\"e\"]/ancestor::td/following-sibling::td[1]")
#   def epoch_osculation(self): return self.driver.find_element_by_xpath("//b[contains(text(),\"Orbital Elements at\")]")
#   def semi_major_axis(self): return self.driver.find_element_by_xpath("//a[text()=\"a\"]/ancestor::td/following-sibling::td[1]")
#


from selenium.webdriver.common.by import By
from adam.nasa_asteroids.pages.page import Page


class AsteroidPage(Page):

    def __init__(self, context):
        super(Page, self).__init__(context=context)

        self.url = "/company-research"

        self.live_availability_option = (By.XPATH, "//option[@value='Live']")

        self.eccetricity = (By.XPATH, '//a[text()=\"e\"]/ancestor::td/following-sibling::td[1]')
        self.epoch_osculation = (By.XPATH, '//b[contains(text(),\"Orbital Elements at\")]')
        self.semi_major_axis = (By.XPATH, '//a[text()=\"a\"]/ancestor::td/following-sibling::td[1]')
