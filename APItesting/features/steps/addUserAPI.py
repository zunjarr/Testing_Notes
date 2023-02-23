from behave import *
import requests
import allure
from POST_Request.payloads import *
from utilities.resources import *
from utilities.configuration import *

# POST creates a resource.
# PUT replaces a resource. PUT replaces the entire resource with given data
# PATCH updates a resource. PATCH replaces only specified fields


@given('User details are provided')
def step_impl1(context):
    context.url_base = getConfig()
    # print('Base url is ', context.url_base)
    context.info_to_post = ApiResources.post_info
    # print('info_to_post is ', context.info_to_post)


@when('Run the post method to add user')
def step_impl2(context):
    context.post_resp = requests.post(getConfig() + context.info_to_post, json=add_user_payload(), )
    # print('status_code is ', context.post_resp.status_code)
    # print('post_resp is ', context.post_resp)


@then('Verify user added successfully')
def step_impl3(context):
    assert context.post_resp.status_code == 201, allure.attach("Resource is not created")

# Commands to execute
# behave features/addUserAPI.feature --no-capture
# behave features/addUserAPI.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
