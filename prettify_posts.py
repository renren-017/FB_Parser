import json
import pandas as pd

from datetime import datetime

with open('prep_json/CalamKyrgyzstan.json') as file:
    data = json.load(file)

urls = []
contents = []
dates = []
columns = ['Url', 'Content', 'Date']
months = {
    'январь': '01',
    'февраль': '02',
    'март': '03',
    'апрель': '04',
    'май': '05',
    'июнь': '06',
    'июль': '07',
    'август': '08',
    'сентябрь': '09',
    'октябрь': '10',
    'ноябрь': '11',
    'декабрь': '12',
}

for url, value in data.items():

    text, date = value['Content'], value['Date']

    if date.endswith('г.'):
        day, month, year, _ = date.split()
        date = f"{year}-{months[month]}-{int(day):02d}"
    elif date.endswith('д.'):
        day, _ = date.split()
        date = f"2023-01-{datetime.now().day-(int(day)):02d}"
    elif date.endswith('ч.'):
        print(date)
        day, _ = date.split()
        date = "2023-01-29"
    elif date == '':
        pass
    elif len(date.split())==4:
        print(date)
        day, month, p, _ = date.split()
        date = f"2023-{months[month]}-{int(day):02d}"
    else:
        day, month, year, _,  _, _ = date.split()
        date = f"{year}-{months[month]}-{int(day):02d}"

    urls.append(url)
    contents.append(text)
    dates.append(date)

df = pd.DataFrame(list(zip(urls, contents, dates)), columns=columns)
df.to_excel(f'data/CalamKyrgyzstan.xlsx', index=False)
