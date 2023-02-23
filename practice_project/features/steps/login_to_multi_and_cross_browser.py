import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import allure_behave
import time
from utilities.urls import DifferentUrl
from utilities.configu import *
from PageObjectModule.Locators.locator import *
# import xdist
# import prettytable
import threading
import multiprocessing


@given('Launch the browsers')
def launch_browsers(context):
    # print('step 1')
    # context.serv_obj = Service('C:\\Users\\dorugzu\\Downloads\\chromedriver_107\\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=context.serv_obj)
    context.driver_chrome = webdriver.Chrome()


@when('Read login details from the csv')
def read_login_credentials(context):
    # print('step 2')
    context.df = read_data()
    context.username_textbox_id = Locator.username_textbox_id
    context.password_textbox_id = Locator.password_textbox_id
    context.login_button_name = Locator.login_button_name


@then('login_with_chrome_browser')
def login_with_chrome_browser(context):
    # print('step 3')
    try:
        for index, row in context.df.iterrows():
            context.driver_chrome.get(DifferentUrl.url_facebook)
            context.driver_chrome.find_element(By.ID, f'{context.username_textbox_id}').send_keys(row['username'])
            context.driver_chrome.find_element(By.ID, f'{context.password_textbox_id}').send_keys(row['password'])
            context.driver_chrome.find_element(By.NAME, f'{context.login_button_name}').click()
            time.sleep(3)
            # context.driver_firefox.get(DifferentUrl.url_facebook)
            # context.driver_firefox.find_element(By.ID, f'{context.username_textbox_id}').send_keys(row['username'])
            # context.driver_firefox.find_element(By.ID, f'{context.password_textbox_id}').send_keys(row['password'])
            # context.driver_firefox.find_element(By.NAME, f'{context.login_button_name}').click()
            # time.sleep(3)
            # print('Scenario ran successfully ')
    except Exception as e:
        print('Getting Error as ', e)
        allure.attach(f'Getting error as {e}')


@then('login_with_firefox_browser')
def login_with_firefox_browser(context):
    # print('step 3')
    context.driver_firefox = webdriver.Firefox()
    context.driver_firefox.maximize_window()
    try:
        for index, row in context.df.iterrows():

            context.driver_firefox.get(DifferentUrl.url_facebook)
            context.driver_firefox.find_element(By.ID, f'{context.username_textbox_id}').send_keys(row['username'])
            context.driver_firefox.find_element(By.ID, f'{context.password_textbox_id}').send_keys(row['password'])
            context.driver_firefox.find_element(By.NAME, f'{context.login_button_name}').click()
            print('Scenario ran successfully ')
    except Exception as e:
        print('Getting Error as ', e)
        allure.attach(f'Getting error as {e}')


# n = 1
# for i in range(n):
#     t1 = threading.Thread(target=login_with_firefox_browser)
#     t2 = threading.Thread(target=login_with_chrome_browser)
#     t1.start(), t2.start()

processes = []
br = [login_with_firefox_browser, login_with_chrome_browser]
for i in range(2):
    p1 = multiprocessing.Process(target=login_with_firefox_browser, args=(br,))
    processes.append(p1)

    p1.start()

@then('Check vpn error')
def check_vpn_error(context):
    # print('step 4')
    try:
        context.driver_chrome.get(DifferentUrl.url_vpn)
        time.sleep(2)
    except Exception as e:
        print('Getting Error as ', e)
        allure.attach(f'Getting VPN error as {e}')


@then('Close the browsers and generate report')
def close_browsers(context):
    context.driver_chrome.close()
    context.driver_firefox.close()
