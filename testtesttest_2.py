import time
from selenium import webdriver
from threading import Thread
from selenium.webdriver.common.by import By

# def func(number):
#     driver = webdriver.Chrome()
#     #driver.set_window_size(920, 680)
#     driver.get(url)
#
#     driver.find_element(By.ID, "email").send_keys("xx")
#     driver.find_element(By.ID, "pass").send_keys("yy")
#     b = driver.find_element(By.ID, "u_0_5_sn")
#
#     buttons[number] = True
#     print(buttons)
#
#     # wait for other buttons
#     while not all(buttons):
#         pass
#
#     print('click', number)
#     b.click()
#
# # ---
#
# url = 'https://www.facebook.com/'
#
# number_of_threads = 5
#
# #buttons = [False * number_of_threads] # create place
# buttons = []
#
# threads = []
#
# for number in range(number_of_threads):
#     t = Thread(target=func, args=(number,)) # get number for place in list `buttons`
#     t.start()
#     threads.append(t)
#     buttons.append(False) # create place
#
# for t in threads:
#     t.join()

# ------------------------------------------------------------------------
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import threading
from selenium.webdriver.chrome.service import Service

# def create_driver():
#     """returns a new chrome webdriver"""
#     chromeOptions = webdriver.ChromeOptions()
#     chromeOptions.add_argument("--headless")  # make it not visible, just comment if you like seeing opened browsers
#     return webdriver.Chrome(options=chromeOptions)
#
#
# def get_title(url, webdriver=None):
#     """get the url html title using BeautifulSoup
#    if driver is None uses a new chrome-driver and quit() after
#    otherwise uses the driver provided and don't quit() after"""
#
#     def print_title(driver):
#         driver.get(url)
#         soup = BeautifulSoup(driver.page_source, "lxml")
#         item = soup.find('title')
#         print(item.string.strip())
#
#     if webdriver:
#         print_title(webdriver)
#     else:
#         webdriver = create_driver()
#         print_title(webdriver)
#         webdriver.quit()
#
#
# links = ["https://www.amazon.com", "https://www.google.com", "https://www.youtube.com/", "https://www.facebook.com/",
#          "https://www.wikipedia.org/",
#          "https://us.yahoo.com/?p=us", "https://www.instagram.com/", "https://www.globo.com/",
#          "https://outlook.live.com/owa/"]


# serv_obj = Service('C:\\Users\\dorugzu\\Downloads\\chromedriver_107\\chromedriver.exe')
# driver = webdriver.Chrome(service=serv_obj)
# driver_chrome = webdriver.Chrome()


# class ChromeOptions:
#     pass


# class ChromeOptions:
#     options = ChromeOptions()
#     options.add_argument("--start-maximized")
#     # driver = ChromeDriver(options)
#     driver = webdriver.Chrome(service=serv_obj, options)
# -----------------------------------------------------------------
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# # maximized window
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com/')
# -----------------------------------------------------------------

import multiprocessing
import concurrent.futures

start = time.perf_counter()


def fun():
    print(f'hello')
    time.sleep(1)
    return f'yellow'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(fun, secs)

    # for res in results:
    #     print(res)

if __name__ == '__main__':
    executors_list = fun()
    for output in executors_list:
        print(output.result())

    # for res in results:
    #     print(res)

# -----------------------------------------------------------------

# num = 4
# p1 = Process(target=fun, args=(num,))
# p1 = multiprocessing.Process(target=fun)
# p1.start()
# p2 = multiprocessing.Process(target=fun)
# p2.start()

# p1.join()
# p2.join()
# -----------------------------------------------------------------

# processes = []
# for _ in range(10):
#     p1 = multiprocessing.Process(target=fun)
#     p1.start()
#     processes.append(p1)
#
# for process in processes:
#     process.join()
# -----------------------------------------------------------------


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f1 = executor.submit(fun, 1)
#     f2 = executor.submit(fun, 1)
#
#     print(f1.result())
#     print(f2.result())
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# p3 = multiprocessing.Process(target=fun)
# p4 = multiprocessing.Process(target=fun)
# p5 = multiprocessing.Process(target=fun)
# p6 = multiprocessing.Process(target=fun)
# p7 = multiprocessing.Process(target=fun)
# p8 = multiprocessing.Process(target=fun)
# p9 = multiprocessing.Process(target=fun)
# p10 = multiprocessing.Process(target=fun)


# p3.start()
# p4.start()
# p5.start()
# p6.start()
# p7.start()
# p8.start()
# p9.start()
# p10.start()


finish = time.perf_counter()
t = finish - start

# if __name__ == '__main__':
#     main()
print(f'total time taken: ', t)

# ---------------------------------
# s1 = {1, 2, 3, {1, 2, 3}}
# print(s1)                     # TypeError: unhashable type: 'set'

s2 = {1, 2, 3, (1, 2, 3)}
print(s2)

# s3 = {1, 2, 3, [1, 2, 3]}
# print(s3)                     # TypeError: unhashable type: 'list'

# s4 = {1, 2, 3, {'a': 'abc'}}
# print(s4)                     # TypeError: unhashable type: 'dict'

s5 = {1, 2, 3, 1, 2, 3, 4, 5}
print(s5)  # {1, 2, 3, 4, 5}
# ---------------------------------
s6 = (1, 2, 3, (1, 2, 3), [1, 2, 3])
s7 = [(1, 2, 3, (1, 2, 3), [1, 2, 3])]
print(s6, s7)

d1 = {[1, 2, 3]: 'abc', }

d2 = [5, 4, 7, 3, 8, 2, 9, 1]
d3 = sorted(d2)
print(d3)  # [1, 2, 3, 4, 5, 7, 8, 9]
# sort(d2)

z = d2.sort()
print(z)  # None
# ---------------------------------
c, d = 10, 10
print(c == d)  # True
print(c is d)  # True
# ---------------------------------
d9 = [5, 7, 3, 6, 2, 9, 1]
d9.sort()
print(d9)  # [1, 2, 3, 5, 6, 7, 9]
k = d9[len(d9) // 2]
print(k)  # 5
# ---------------------------------

y = 'stuff;thing;junk;'
z = y.split(';')
print('after splitting: ', z)  # ['stuff', 'thing', 'junk', '']
print(len(z))  # 4
# ---------------------------------

print(5 != 6)  # True
# ---------------------------------

print(list(reversed(range(1, 11))))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ---------------------------------

Mylist = [2, 'Apple', 3.4]
Mylist[1] = 'orange'
print(Mylist)  # [2, 'orange', 3.4]
# ---------------------------------

num_list = [1, 2, 3, 4, 5]
num_list.remove(4)
print(num_list)  # [1, 2, 3, 5]
# ---------------------------------

from multiprocessing import Process


def func1():
    print('func1: starting')
    for i in range(10000000): pass
    print('func1: finishing')


def func2():
    print('func2: starting')
    for i in range(10000000): pass
    print('func2: finishing')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
# ---------------------------------------------

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
# ---------------------------------------------
from selenium import webdriver
import threading
import time
import csv
import pandas as pd
import multiprocessing
# Cross browser parallel testing


def test_multi_browse_chrome():
    driver = webdriver.Chrome()
    # options = ChromeOptions()
    # options.add_argument("--start-maximized")
    # driver = ChromeDriver(options)
    driver.get('https://www.amazon.com/')
    driver.get('https://www.facebook.com/')
    driver.get('https://www.flipkart.com/')
    driver.get('https://www.yatra.com/')
    driver.get('https://www.twitter.com/')
    driver.get('https://www.youtube.com/')
    driver.quit()
    print("Run successfully on Chrome")

def test_multi_browse_firefox():
    driver_firefox = webdriver.Firefox()
    driver_firefox.get('https://www.yatra.com/')
    driver_firefox.get('https://www.twitter.com/')
    driver_firefox.get('https://www.youtube.com/')
    driver_firefox.get('https://www.flipkart.com/')
    driver_firefox.get('https://www.facebook.com/')
    driver_firefox.get('https://www.amazon.com/')
    driver_firefox.quit()
    print("Run successfully on Firefox")

def test_multi_browse_edge():
    driver_edge = webdriver.Edge()
    driver_edge.get('https://www.yatra.com/')
    driver_edge.get('https://www.twitter.com/')
    driver_edge.get('https://www.youtube.com/')
    driver_edge.get('https://www.flipkart.com/')
    driver_edge.get('https://www.facebook.com/')
    driver_edge.get('https://www.amazon.com/')
    driver_edge.quit()
    print("Run successfully on Edge")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=test_multi_browse_firefox)
    p1.start()
    p2 = multiprocessing.Process(target=test_multi_browse_chrome)
    p2.start()
    p3 = multiprocessing.Process(target=test_multi_browse_edge)
    p3.start()
    p1.join()
    p2.join()
    p3.join()
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

