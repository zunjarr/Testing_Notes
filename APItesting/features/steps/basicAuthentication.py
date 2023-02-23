import allure
from behave import *
import requests
from utilities.configuration import *
from requests.auth import HTTPBasicAuth


@given('Provided user credentials')
def step_impl1(context):
    context.fetched_token = getToken()
    print(context.fetched_token)


@when('Run the get method')
def step_impl2(context):
    context.respo_atlass = requests.get(getAuthUrl(), auth=('codewithderrick@gmail.com', context.fetched_token))
    # print('respo_atlass is ', context.respo_atlass)


@then('Verify successful authentication')
def step_impl3(context):
    # allure.attach("Authentication is failed")
    assert context.respo_atlass.status_code == 300, allure.attach("Authentication is failed")

# Commands to execute
# behave features/basicAuthentication.feature --no-capture
# behave features/basicAuthentication.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
