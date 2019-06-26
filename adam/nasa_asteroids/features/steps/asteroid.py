from behave import *
from data.config import settings
import requests
import json
import re
import jsonpath_rw_ext as jp
from utilities.asteroids import asteroid


# No need for global variables in Steps files. Use context.{some_variable_name}
# url = ""
# response = None
# data = []
# errors = []


"""

NOTES: 

1) Make all function names as descriptive as possible, try and avoid default 'step_impl'

2) We'll use regex for all step matching. 

3) Python conventionally uses snake_case

"""


@given('we have called the api')
def step_impl(context):
    pass


@given("a response from the NASA API")
def step_impl(context):
    context.response = requests.request("GET",
                                        settings['url']['root'] +
                                        settings['url']['path']['asteroids'][
                                            'septemberAsteroids'])


@when('the service method is GET')
def step_impl(context):
    pass


@then('the Response call should be 200')
def step_impl(context):
    data = context.response.json()
    context.data = jp.match("$.near_earth_objects.*.[*]", data)
    # After we declare these variables "into context" we have them for the rest of the test
    assert context.response.status_code is 200


@then('the required data should be present')
def step_impl(context):
    counter = 0
    for f in context.data:
        if f['id'] is None:
            context.errors.append('ID is empty at index ' + str(counter))
        if f['name'] is None:
            context.errors.append('Name is empty at index ' + str(counter))
        if f['nasa_jpl_url'] is None:
            context.errors.append(
                'nasa_jpl_url is empty at index ' + str(counter))
        if f['estimated_diameter'] is None:
            context.errors.append(
                'estimated_diameter is empty at index ' + str(counter))
        counter += 1


@then('the Nasa Jpl Url should have correct format')
def step_impl(context):
    counter = 0

    for f in context.data:
        if re.match(settings['regex']['url'], f['nasa_jpl_url']) is None:
            context.errors.append(
                'nasa_jpl_url is not the correct format ' + str(counter))
        counter += 1


@then('the Absolute Magnitude should be decimal')
def step_impl(context):
    counter = 0

    for f in context.data:
        if type(f['absolute_magnitude_h']) != float:
            context.errors.append(
                'Absolute magnitude is not a decimal at index ' + str(counter))
        counter += 1


@then('the Estimated Diameter Max should be greater than the Estimated Diameter Min')
def step_impl(context):
    context.counter = 0

    for f in context.data:
        if f['estimated_diameter']['kilometers']['estimated_diameter_min'] > \
                f['estimated_diameter']['kilometers']['estimated_diameter_max']:
            context.errors.append(
                'Estimated Diamteer Min is greater than Estimated Diamteer Max at index ' + str(
                    context.counter))
        context.counter += 1


@then('the Estimated Diameters in miles should be the same in meters')
def step_impl(context):
    counter = 0

    for f in context.data:
        if round(f["estimated_diameter"]["kilometers"]["estimated_diameter_min"] * 1000) != round(
                f["estimated_diameter"]["meters"]["estimated_diameter_min"]):
            context.errors.append(
                'Estimated Diamters are not equal in kilometers and meters at index ' + str(
                    counter))
        counter += 1


@then('the Is Potentially Hazardous Asteroid should be boolean')
def step_impl(context):
    counter = 0

    for f in context.data:
        if type(f['is_potentially_hazardous_asteroid']) != bool:
            context.errors.append(
                'Is Potentially Hazardous Asteroid is not boolean at index ' + str(counter))
        counter += 1


@then('the Close Approach Date should exist if the Approach Data exists')
def step_impl(context):
    counter = 0

    for f in context.data:
        if f['close_approach_data']:
            for a in f['close_approach_data']:
                if not a['close_approach_date']:
                    context.errors.append(
                        'The Close Approach Date does not exist at index ' + str(counter))
                counter += 1


@then('the Orbiting Body should exist if the Approach Data exists')
def step_impl(context):
    counter = 0

    for f in context.data:
        if f['close_approach_data']:
            for a in f['close_approach_data']:
                if not a['orbiting_body']:
                    context.errors.append(
                        'The Orbiting Body does not exist at index ' + str(counter))
                counter += 1


@given('I have the asteroid API data')
def step_impl(context):
    pass


@when('I am on the asteroid page')
def step_impl(context):
    pass


@then('the asteroid should have the same data as the API')
def step_impl(context):
    asteroid.verify_asteroid(context.data, context.errors)

    if context.errors != []:
        assert False, context.errors
