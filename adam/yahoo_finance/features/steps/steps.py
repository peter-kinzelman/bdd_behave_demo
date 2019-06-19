from behave import *
import requests
from utilities.stocks import yahoo
from data.config import settings
import time

errors = []

@given('we have called the api')
def step_impl(context):
  global url
  url = settings['url']['root'] + settings['url']['stocks_path']

@when('the service method is GET')
def step_impl(context):
  pass

@then('the Response call should be 200')
def step_impl(context):
  global response
  response = requests.request("GET", url)
  global data
  data = response.json()
  print(data)
  assert response.status_code is 200

@then('the required data should be present')
def step_impl(context):
  counter = 0 

  for f in data:
    if f['symbol'] is None: errors.append('Symbol is not present at index ' + str(counter))
    if f['price'] is None: errors.append('Price is empty at ' + counter)
    if f['size'] is None: errors.append('Size is empty at ' + counter)
    if f['time'] is None: errors.append('Time is empty at ' + counter)
    counter += 1

@then('the symbol should be a unicode')
def step_impl(context):
  counter = 0

  for f in data:
    if type(f['symbol']) != unicode: errors.append('Symbol is not a unicode at index ' + str(counter))
    counter += 1

@then('the price should be a decimal')
def step_impl(context):
  counter = 0

  for f in data:
    if type(f['price']) != float: errors.append('Price is not a decimal at index ' + str(counter))
    counter += 1

@given('I am on the yahoo web page')
def step_impl(context):
  yahoo.get_yahoo_stocks()

@when('I am on the company page')
def step_impl(context):
  yahoo.get_company_page(data, errors)

@then('the page should have the same data as the API')
def step_impl(context):

    yahoo.verify_ui_data(data, errors)

    if errors != []: 
      assert False, errors
