import json
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


proxy_url = ""

options = Options()
options.add_argument('--no-sandbox')
options.add_argument(f"--proxy-server={proxy_url}")
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

# driver.get("https://www.facebook.com/login/")
# # print(driver.title)
# driver.find_element(By.XPATH, "//input[@id='email' and @name='email']").send_keys("")
# driver.find_element(By.XPATH, "//input[@id='pass' and @name='pass']").send_keys("")
# # driver.find_element(By.ID, "loginbutton").click()
# form = driver.find_element(By.ID, "login_form")
# form.submit()


def openSeeMore(browser):
    readMore = browser.find_elements(By.XPATH, "//div[text()='Ещё']")
    if len(readMore) > 0:
        count = 0
        for i in readMore:
            action = ActionChains(browser)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    browser.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(readMore) - count > 0:
            print('readMore issue:', len(readMore) - count)
            pass
        time.sleep(1)
    else:
        pass


print(driver.title)
print(driver.current_url)

driver.get("https://www.facebook.com/CalamKyrgyzstan/")
el = driver.find_elements(By.XPATH, "//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3']")
for e in el:
    if e.text == 'Фильтры':
        action = ActionChains(driver)
        action.move_to_element(e).click().perform()
        time.sleep(3)
        el_b = driver.find_elements(By.XPATH,
                                  "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1hl2dhg xggy1nq x1t137rt x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz x6s0dn4 xjyslct x1qhmfi1 xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk x1qughib xdj266r x11i5rnm xat24cr x1mh8g0r x889kno xn6708d x1a8lsjc x1ye3gou x1n2onr6 x1yc453h x1ja2u2z']")
        for eb in el_b:
            if eb.text == 'Год':
                action.move_to_element(eb).click().perform()
                time.sleep(3)
                readMore = e.find_elements(By.XPATH, "//*[text()='2022']")
                action.move_to_element(readMore[0]).click().perform()
                time.sleep(3)
        el_b = driver.find_elements(By.XPATH,
                                    "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1hl2dhg xggy1nq x1t137rt x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz x6s0dn4 xjyslct x1qhmfi1 xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk x1qughib xdj266r x11i5rnm xat24cr x1mh8g0r x889kno xn6708d x1a8lsjc x1ye3gou x1n2onr6 x1yc453h x1ja2u2z']")
        for eb in el_b:
            if eb.text == 'Месяц':
                action.move_to_element(eb).click().perform()
                time.sleep(3)
                readMore = e.find_elements(By.XPATH, "//*[text()='сентябрь']")
                action.move_to_element(readMore[0]).click().perform()
                time.sleep(3)

        ready = e.find_elements(By.XPATH, "//*[text()='Готово']")
        action.move_to_element(ready[1]).click().perform()
        time.sleep(3)


count = 0
switch = True
old_numReviews = 0
specifiedNumber = 5
contents = []
urls = []
dates = []
columns = ['Url', 'Content', 'Date']

while switch:
    count += 1
    # getBack(driver)

    # scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(8)

    # process check
    reviewList = driver.find_elements(By.XPATH, "//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
    for review in reviewList[old_numReviews:len(reviewList)]:

        span = review.find_element(By.CSS_SELECTOR,
                                   "a[class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm']")
        url = span.get_attribute('href')
        if url in urls:
            continue

        date = span.text
        try:
            name = review.find_element(By.CSS_SELECTOR,
                                       "span[class='x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h']").text
        except:
            continue

        urls.append(url)
        if 'Ещё' in name:
            openSeeMore(driver)
            # name = review.find_element(By.CSS_SELECTOR,
            #                            "span[class='x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h']").text
        contents.append(name)
        dates.append(date)

    numReviews = len(reviewList)
    if old_numReviews < numReviews:
        print('Scroll Count:', count, '  numReviews:', numReviews)
    old_numReviews = numReviews

    # termination condition
    if numReviews >= specifiedNumber:
        try:
            print(f'Done {specifiedNumber} reviews')
            specifiedNumber += 5

            with open('missed.json') as f:
                existed = json.load(f)

            for i in range(len(urls)):
                existed[urls[i]] = {
                        'Content': contents[i],
                        'Date': dates[i]
                }

            with open('missed.json', 'w', encoding='utf8') as f:
                json.dump(existed, f, indent=4, ensure_ascii=False)

            contents = []
            urls = []
            dates = []
        except:
            print('Err: Loading data to json')
