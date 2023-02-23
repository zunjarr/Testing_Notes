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


# def read_csv_data():
# with open('C:\\Users\\dorugzu\\practice_project\\test_data\\test_data.csv',) as csvFile:
#     csvReader = csv.reader(csvFile, delimiter=',')
#     # print(csvReader)
#     # print(type(csvReader))
#
#     brwr = []
#     user = []
#     pswd = []
#     for row in csvReader:
#         # print(row)
#         brwr.append(row[0])
#         user.append(row[1])
#         pswd.append(row[2])
#         print('brwr is : ', brwr)
#         print('user is : ', user)
#         print('pswd is : ', pswd)
#         index = brwr.index('browser')
#         print('index is : ', index)
#         browser = brwr[index]
#         username = user[index]
#         password = pswd[index]
#         print('Value in browser is: ', browser)
#         print('Value in username is: ', username)
#         print('Value in password is: ', password)

# df_csv2 = pd.read_csv('C:\\Users\\dorugzu\\practice_project\\test_data\\test_data.csv', )
# print(type(df_csv2))
# # df = pd.DataFrame(df_csv2)
# # print(df)
# lis_dic2 = df_csv2.to_dict('records')
# print(lis_dic2)
# # print(type(lis_dic2))
# # print(lis_dic2[0])
#
# for ele in lis_dic2:
#     browser_name = ele['browser']
#     username = ele['username']
#     password = ele['password']
#
#     # print('browser_name is: ', browser_name)
#     # print('username is: ', username)
#     # print('password is: ', password)
#
#     if 'chrome' == browser_name:
#         driver_chrome = webdriver.Chrome()
#         driver_chrome.get('https://www.tweeter.com/')
#         print('username is: ', username)
#         print('password is: ', password)
#         # break
#     elif 'firefox' == browser_name:
#         driver_firefox = webdriver.Chrome()
#         driver_firefox.get('https://www.facebook.com/')
#         print('username is: ', username)
#         print('password is: ', password)
#         # break
#     elif 'edge' == browser_name:
#         driver_edge = webdriver.Chrome()
#         driver_edge.get('https://www.yatra.com/')
#         print('username is: ', username)
#         print('password is: ', password)
#         # break
#     elif 'opera' == browser_name:
#         driver_opera = webdriver.Chrome()
#         driver_opera.get('https://www.youtube.com/')
#         print('username is: ', username)
#         print('password is: ', password)
#         break


# n = 1
# thread_list = list()
#
# for i in range(n):
#     t1 = threading.Thread(name='Test {}'.format(i), target=test_multi_browse_chrome)
#     t2 = threading.Thread(name='Test {}'.format(i), target=test_multi_browse_firefox)
#     t1.start(), t2.start()
#     # print(t1.name + ' started!'), print(t2.name + ' started!')
#     # thread_list.append(t1), thread_list.append(t2)
