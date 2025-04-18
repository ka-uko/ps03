from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#Создадим отдельную переменную text, куда будут сохраняться все цитаты
text = soup.find_all("span", class_="text") #find ищет первое попавшееся,  find_all - ищет все


#Создадим отдельную переменную author, куда будут сохраняться все авторы
author = soup.find_all("small", class_="author")

#С помощью функции range(len) определим общее количество цитат
for i in range(len(text)):
#Присвоим номер каждой цитате так, чтобы нумерация шла с 1
    print(f"Цитата номер - {i + 1}")
#Выводим саму цитату, указывая её id
    print(text[i].text)
#Выводим автора цитаты
    print(f"Автор цитаты - {author[i].text}\n")