from behave import *
import requests
import allure
from POST_Request.payloads import *
from utilities.resources import *
from utilities.configuration import *


@given(u'Provided data to update info of user')
def step_impl1(context):
    context.url_base = getConfig()
    # print('Base url is ', context.url_base)
    context.info_to_update = ApiResources.put_update_info
    # print('info_to_update is ', context.info_to_update)


@when(u'Run the put method')
def step_impl2(context):
    context.response_put = requests.put(getConfig() + context.info_to_update, data=update_user_payload())
    # print('put response is ', context.response_put)


@then(u'Verify updated data of user')
def step_impl3(context):
    assert context.response_put.status_code == 300, allure.attach("Resource is not created")

# Commands to execute
# behave features/updateUserDetails.feature --no-capture
# behave features/updateUserDetails.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
