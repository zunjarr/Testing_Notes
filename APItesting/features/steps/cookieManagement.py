from behave import *
import requests
from utilities.configuration import *
from utilities.resources import *


@given('Provide input details')
def step_impl1(context):
    context.se = requests.session()
    context.se.cookies.update({'visit-month': 'April'})  # Common cookie


@when('Run get method')
def step_impl2(context):
    context.respo_cooki = requests.get(ApiResources.cookie_url, cookies={'visit-year': '2022'})
    context.respo_cooki_se = context.se.get(ApiResources.cookie_url, cookies={'visit-year': '2022'})


@then('Verify the cookie')
def step_impl3(context):
    # print('respo_cooki is ', context.respo_cooki.text)
    print('respo_cooki_se is ', context.respo_cooki_se.text)

# Commands to execute
# behave features/cookieManagement.feature --no-capture
# behave features/cookieManagement.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
