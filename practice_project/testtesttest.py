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
