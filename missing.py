import json
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


proxy_url = ""

options = Options()
options.add_argument('--no-sandbox')
options.add_argument(f"--proxy-server={proxy_url}")
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

with open('prep_json/CalamKyrgyzstan.json') as file:
    reviewList = json.load(file)

cnt = 0
for url, values in reviewList.items():

    if not values['Content'] == "":
        continue
    driver.get(url)
    time.sleep(1)
#     # action = ActionChains(driver)
#     # try:
#     #     readMore = driver.find_elements(By.XPATH, "//div[text()='Ещё']")
#     #     action.move_to_element(readMore[1]).click().perform()
#     # except:
#     #     continue
    try:
        span = driver.find_element(By.CSS_SELECTOR,
                                   "a[class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm']")

    except:
        continue
    date = span.text
    try:
        name = driver.find_element(By.CSS_SELECTOR,
                                   "span[class='x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u']").text

        # if name.startswith('Салам Кыргызстан'):
        #     continue
    except:
        continue

    reviewList[url] = {
        'Content': name,
        'Date': date
    }

    print(reviewList[url])

    if cnt % 20 == 0:
        with open('prep_json/CalamKyrgyzstan.json', 'w', encoding='utf8') as f:
            json.dump(reviewList, f, indent=4, ensure_ascii=False)
        print(cnt)

    cnt += 1

with open('prep_json/CalamKyrgyzstan.json', 'w', encoding='utf8') as f:
    json.dump(reviewList, f, indent=4, ensure_ascii=False)