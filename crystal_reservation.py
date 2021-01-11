from selenium import webdriver
import time
import argparse
import numpy as np
import sys



if sys.stdin.isatty():
    print('running in CLI')
    parser = argparse.ArgumentParser(description='Bot to make ski reservation at Crystal')
    parser.add_argument('Date', metavar='date',
                           type=str,
                           help='the date of the current month to reserve; format e.g.: Mon Jan 11 2021')

    parser.add_argument('UserName', metavar='user',
                           type=str,
                           help='User Name for Ikon Login')

    parser.add_argument('Password', metavar='pass',
                           type=str,
                           help='Password for Ikon Login')
    args = parser.parse_args()

    user = args.UserName
    pw = args.Password
    date = args.Date

else:
    print('running interactively')
    user = ''
    pw = ''
    date = ''


def get_rand():
    num = 3 * np.random.rand(1)[0]
    return max(num, 2)


failcount = 0

while True:

    try:
        driver = webdriver.Chrome(executable_path="C:\\Users\\chrledw\\PycharmProjects\\chromedriver.exe")
        driver.get("https:/account.ikonpass.com/en/myaccount")
        time.sleep(get_rand())
        emailfield = driver.find_element_by_id("email")
        passfield = driver.find_element_by_id("sign-in-password")

        emailfield.clear()
        emailfield.send_keys(user)
        # emailfield.send_keys(args.UserName)

        passfield.clear()
        passfield.send_keys(pw)
        # passfield.send_keys(args.Password)

        enterbutton = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/section/div/div/div/div[1]/div/div/div[1]/div/form/button")
        enterbutton.click()

        time.sleep(get_rand())

        resurl = 'https://account.ikonpass.com/en/myaccount/add-reservations/'
        driver.get(resurl)

        time.sleep(get_rand())

        crystal = driver.find_element_by_id("react-autowhatever-resort-picker-section-4-item-0")
        crystal.click()
        time.sleep(get_rand())

        continuebutton = driver.find_element_by_xpath('/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[2]/div[2]/button')
        continuebutton.click()

        time.sleep(get_rand())
        print(F"Trying to get reservation for {date}")

        dayobj = driver.find_element_by_xpath(F"//div[@aria-label='{date}']")
        dayobj.click()
        # day11 = driver.find_element_by_xpath('/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]')
        # day11.click()

        time.sleep(get_rand())
        savebutton = driver.find_element_by_xpath("/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[3]/div[1]/div[2]/div/div[4]/button[1]")
        savebutton.click()
        time.sleep(get_rand())
        reviewmyres = driver.find_element_by_xpath('/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[3]/div[2]/button')
        reviewmyres.click()
        time.sleep(get_rand())
        checkbox = driver.find_element_by_xpath("/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[4]/div/div[4]/label/input")
        checkbox.click()
        time.sleep(get_rand())
        confirmbutton = driver.find_element_by_xpath("/html/body/div[3]/div/div/main/section[2]/div/div[2]/div[4]/div/div[5]/button")
        confirmbutton.click()
        time.sleep(get_rand())
        finishbutton = driver.find_element_by_xpath("/html/body/div[4]/div/div/main/section[2]/div/div/div[3]/a[1]")
        finishbutton.click()
        time.sleep(get_rand())
        print(F'SUCCESS, YOUVE GOT A RESERVATION FOR THE DAY: {date}')
        sys.exit()

    except:
        failcount = failcount + 1
        print(failcount)
        driver.close()
        wait = 300 * np.random.rand(1)[0]
        print("waiting: " + str(wait))
        time.sleep(wait)
        continue

