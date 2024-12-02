import json
import requests
from bs4 import BeautifulSoup as bs

main_url = 'https://eda.ru/recepty/afishaeda/russkaya-kuhnya/osnovnye-blyuda'
result = []

for i in range(2):
    req = requests.get(f'{main_url}?page={i}').text
    soup = bs(req, 'lxml')

    check = soup.find_all('div', 'emotion-1j5xcrd')
    for z in check:
        url_to_nameprod = z.find('a').get('href')
        full_info = requests.get(f'https://eda.ru{url_to_nameprod}').text

        soup_2 = bs(full_info, 'lxml')

        name_prod = soup_2.find('h1', 'emotion-gl52ge').text
        callories = soup_2.find('div', 'emotion-16si75h').find('span', itemprop='calories').text
        weight_1 = soup_2.find_all('div', 'emotion-1huad2w')[4].find('span').text
        protein = soup_2.find_all('div', 'emotion-16si75h')[1].find('span', itemprop='proteinContent').text
        weight_2 = soup_2.find_all('div', 'emotion-1huad2w')[5].find('span').text
        fats = soup_2.find_all('div', 'emotion-16si75h')[2].find('span', itemprop='fatContent').text
        weight_3 = soup_2.find_all('div', 'emotion-1huad2w')[6].find('span').text
        carb = soup_2.find_all('div', 'emotion-16si75h')[3].find('span', itemprop='carbohydrateContent').text
        weight_4 = soup_2.find_all('div', 'emotion-1huad2w')[7].find('span').text
        
        item = {
            'Страница': i,
            'Название продукта': name_prod,
            'Калорийность': f'{callories} {weight_1}',
            'Белки': f'{protein} {weight_2}',
            'Жиры': f'{fats} {weight_3}',
            'Углеводы': f'{carb} {weight_4}'
        }
        result.append(item)

# Открываем файл для записи только один раз за пределами цикла
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)



