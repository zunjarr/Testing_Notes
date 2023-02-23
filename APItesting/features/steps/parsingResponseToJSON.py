from behave import *
import json
import requests
import allure
from utilities.resources import *
import jsonpath


@given('Given input details')
def step_impl1(context):
    context.url_get = ApiResources.url_get_req


@when('Run get method and parse response to JSON format')
def step_impl2(context):
    context.response = requests.get(context.url_get)
    # print("response code is ", context.response.status_code)
    context.json_response = json.loads(context.response.text)
    # print("Parsed response in JSON format is ", context.json_response)
    print("json dumps is ", json.dumps(context.response.json(), indent=4))


@then('Fetch and verify specific value using JSON path')
def step_impl3(context):
    pages = jsonpath.jsonpath(context.json_response, "total_pages")
    assert context.response.status_code == 200, allure.attach("Wrong status code")
    assert pages[0] == 2, allure.attach("Showing wrong data of total_pages")

# Commands to execute
# behave features/parsingResponseToJSON.feature --no-capture
# behave features/parsingResponseToJSON.feature --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
# allure serve .\AllureReports\
