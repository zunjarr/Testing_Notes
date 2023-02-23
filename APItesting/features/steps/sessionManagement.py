from behave import *
import requests
import allure
from utilities.configuration import *
from utilities.resources import *


@given('Provided credentials')
def step_impl1(context):
    context.se = requests.session()
    context.se.auth = auth = ('postman', 'password')
    # context.authcred = auth = ('postman', 'password')
    # print("Postman URL is ", ApiResources.url_postman)


@when('Running get method')
def step_impl2(context):
    context.respo_postman_re = requests.get(ApiResources.url_postman, auth=('postman', 'password'))
    # context.respo_postman_re = requests.get(ApiResources.url_postman, auth=context.authcred)

    # context.respo_postman_se = context.se.get(ApiResources.url_postman, auth=context.authcred)
    context.respo_postman_se = context.se.get(ApiResources.url_postman)


@then('Verify response during the session')
def step_impl3(context):
    # print('respo_postman is ', context.respo_postman_se)
    # assert context.respo_postman_re.status_code == 200, allure.attach("Authentication is failed in this session")
    assert context.respo_postman_se.status_code == 200, allure.attach("Authentication is failed in this session")


# Commands to execute
# behave features/sessionManagement.feature --no-capture

# behave features/sessionManagement.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports

# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
