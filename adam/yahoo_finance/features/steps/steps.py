from behave import *
import requests
import json
import re
import jsonpath_rw_ext as jp
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.constants import *
from zaid.nasa_asteroids.config.constants import Constants
import math

# No need for global variables in Steps files. Use context.{some_variable_name}.

# _result = []
# _url = ""
# _method = ""


"""

NOTES: 

1) Make all function names as descriptive as possible, try and avoid default 'step_impl'

2) We'll use regex for all step matching. 

3) Python conventionally uses snake_case

"""


@given(u'the api service is for : "{endPoint}" stocks')
def step_impl(context, endPoint):
    if endPoint == "SNAP,fb":
        # store endpoints somewhere else, call them by name
        context.url = Constants.FULL_URL + endPoint
    else:
        assert False, "endpoint url is not provided"


@when(u'the service method is "{method}"')
def step_impl(context, method):
    context.method = method


@then(u'the response code should be "{status}"')
def step_impl(context, status):
    context.esponse = requests.request(context.method, context.url)
    context.result = context.response.json()
    # Anything we want to "archive" and validate later just put into context
    assert context.response.status_code is int(status)


@then(u'it should return the datafor "{num}" company')
def step_impl(context, num):
    context.total_number = len(context.result)
    assert str(context.total_number) == str(num)


@then(u'verify required fields')
def step_impl(context):
    errors = []
    counter = 1
    for stock in context.result:
        err = []
        if type(stock['symbol']) is None:
            err.append('stock in index ' + str(counter) +
                       ' dose not have symbol')
        if type(stock['price']) is None:
            err.append('stock in index ' + str(counter) +
                       ' dose not have price')
        counter += 1
        if err != []:
            errors.append(err)
    if errors != []:
        assert False, errors


@given(u'we have the data from the api')
def step_impl(context):
    assert context.result is not None


@then(u'the UI should have the same data as the api')
def step_impl(context):
    errors = []
    counter = 1

    # there has to be a generic method for this
    def floatDigits(f, n):
        return math.floor(f * 10 ** n) / 10 ** n

    # Where are all these CONSTANT values declared?
    for stock in context.result:
        err = []
        browser = Common.chrome()
        browser.get(Constants.YAHOO_URL)
        # All these elements should live on a Page Object
        browser.find_element(
            By.CSS_SELECTOR, SEARCH_INPUT_locator).send_keys(stock["symbol"])
        browser.find_element(By.CSS_SELECTOR, SEARCH_BUTTON_locator).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, PRICE_locator)))
        arr = []
        for x in range(5):
            time.sleep(2)
            price = browser.find_element(By.XPATH, PRICE_locator).text
            arr.append(floatDigits(float(price), 2))

        if round(float(stock["price"]), 2) not in arr:
            err.append(["The two prices is not equal for " + stock["symbol"],
                        arr, round(float(stock["price"]), 2)])

        browser.quit()
        if err != []:
            errors.append(err)
        counter += 1
    if errors != []:
        assert False, errors
