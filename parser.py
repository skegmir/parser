from email import header
from urllib import response
import requests
from bs4 import BeautifulSoup
def get_html(url):
    headers = {"user-agent" : "yandex"}
    response = requests.get(url, headers=headers)
    html = response.text
    return html
def get_weather_now(text) :
    """"получаем погоду на данный момент"""
    url = f"http://avia.meteonovosti.ru/-{text.lower()}"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    try :
        temp = soup.find("div", class_="weather__article_main_temp").get_text(strip=True)
        description = soup.find("div", class_="weather__article_description-text").get_text(strip=True)
        print (f"Температура воздуха сейчас {temp}\n{description}")
    exсept:
        print (f"город"{text}"не найден. Скорее всего вы сделали опечатку")
text = input ( "Введи город, в котором хочешь узнать погоду:" )
get_weather_now(text)
