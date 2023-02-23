from behave import *
import requests
import allure
from utilities.resources import *


@given('Provide the detail')
def step_impl(context):
    context.url_get = ApiResources.url_get_req
    # print("url_get request is ", context.url_get)


@when('Run a get method')
def step_impl(context):
    context.response = requests.get(context.url_get)


@then('Verify the response')
def step_impl(context):
    print("response code is ", context.response)
    print("response code or status_code is ", context.response.status_code)
    print("Content or Body is ", context.response.content)
    print("The Headers are ", context.response.headers)
    assert context.response.status_code == 200, allure.attach("Wrong status_code")

# Commands to execute
# behave features/getRequestVerify.feature --no-capture
# behave features/getRequestVerify.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
