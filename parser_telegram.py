import json
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

with open('prep_json/polit_lombard.json') as file:
    data = json.load(file)

urls = []
contents = []
dates = []
columns = ['Url', 'Content', 'Date']

base_url = "https://t.me/polit_lombard/"

for datagram in data['messages']:
    if datagram['type'] != 'message':
        continue

    if datagram.get('forwarded_from'):
        continue

    date = datagram['date'].split('T')[0]
    url = base_url + str(datagram['id'])
    text = ' '.join([d['text'] for d in datagram['text_entities']])
    if datagram['text'] == '':
        try:
            driver.get(url+'?embed=1&mode=tme')
            text = driver.find_element(By.XPATH, "//div[@class='tgme_widget_message_text js-message_text']").text
        except:
            pass

    urls.append(url)
    contents.append(text)
    dates.append(date)

df = pd.DataFrame(list(zip(urls, contents, dates)), columns=columns)
df.to_excel(f'data/polit_lombard.xlsx', index=False)
