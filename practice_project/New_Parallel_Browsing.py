import time
from threading import Thread
import multiprocessing

# browsers = [{'platform': 'Windows 10', 'browserName': 'Firefox', 'version': '108.0.2', 'name': 'Python Parallel'}, {'platform': 'Windows 10', 'browserName': 'Chrome', 'version': '109.0.5414.75', 'name': 'Python Parallel'}]
#
# browsers_waiting = []
#
# browser_data = ['Firefox', 'Chrome']
#
# def get_browser(browser_data):
#     browser_data = ['Firefox', 'Chrome']
#
#
# def get_browser_and_wait(browser_data):
#     print ("starting %s\n" % browser_data["browserName"])
#     browser = get_browser(browser_data)
#     browser.get("http://crossbrowsertesting.com")
#     browsers_waiting.append({"data": browser_data, "driver": browser})
#     print ("%s ready" % browser_data["browserName"])
#     while len(browsers_waiting) < len(browsers):
#         print ("working on %s.... please wait" % browser_data["browserName"])
#         browser.get("http://crossbrowsertesting.com")
#         time.sleep(3)
#
#
# threads = []
# for i, browser in enumerate(browsers):
#     thread = Thread(target=get_browser_and_wait, args=[browser])
#     threads.append(thread)
#     thread.start()
#     for thread in threads:
#         thread.join()
#         print("all browsers ready")
#
#         for i, b in enumerate(browsers_waiting):
#             print("browser %s's title: %s" % (b["data"]["name"], b["driver"].title))
#             b["driver"].quit()

# ---------------------------------------------
# def useless_function(sec=1):
#     print(f'Sleeping for {sec} second(s)')
#     time.sleep(sec)
#     print(f'Done sleeping')
#
# start = time.perf_counter()
# process1 = multiprocessing.Process(target=useless_function)
# process2 = multiprocessing.Process(target=useless_function)
# process1.start()
# process2.start()
# end = time.perf_counter()
# print(f'Finished in {round(end-start, 2)} second(s)')

# ---------------------------------------------
# from multiprocessing import Pool
# import time
# import math
#
# N = 5000000
#
#
# def cube(x):
#     return math.sqrt(x)
#
#
# if __name__ == "__main__":
#     with Pool() as pool:
#         result = pool.map(cube, range(10, N))
#     print("Program finished!")
# ---------------------------------------------
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
