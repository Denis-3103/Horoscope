import requests
from bs4 import BeautifulSoup as b


url_1 = 'https://horo.mail.ru/prediction/aries/today/' # Овен
url_2 = 'https://horo.mail.ru/prediction/taurus/today/' # Телец
url_3 = 'https://horo.mail.ru/prediction/gemini/today/' # Близнецы
url_4 = 'https://horo.mail.ru/prediction/cancer/today/' # Рак
url_5 = 'https://horo.mail.ru/prediction/leo/today/' # Лев
url_6 = 'https://horo.mail.ru/prediction/virgo/today/' # Дева
url_7 = 'https://horo.mail.ru/prediction/libra/today/' # Весы
url_8 = 'https://horo.mail.ru/prediction/scorpio/today/' # Скорпион
url_9 = 'https://horo.mail.ru/prediction/sagittarius/today/' # Стрелец
url_10 = 'https://horo.mail.ru/prediction/capricorn/today/' # Козерог
url_11 = 'https://horo.mail.ru/prediction/aquarius/today/' # Водолей
url_12 = 'https://horo.mail.ru/prediction/pisces/today/' #


def aries(url_1):
    r = requests.get(url_1)
    soup = b(r.text, 'html.parser')
    aries = soup.find_all('div', class_='article__text')
    all_aries = []
    for i in aries:
        all_aries.append(i.text)
    return all_aries

def taurus(url_2):
    r = requests.get(url_2)
    soup = b(r.text, 'html.parser')
    taurus = soup.find_all('div', class_='article__text')
    all_taurus = []
    for i in taurus:
        all_taurus.append(i.text)
    return all_taurus

def gemini(url_3):
    r = requests.get(url_3)
    soup = b(r.text, 'html.parser')
    gemini = soup.find_all('div', class_='article__text')
    all_gemini = []
    for i in gemini:
        all_gemini.append(i.text)
    return all_gemini

def cancer(url_4):
    r = requests.get(url_4)
    soup = b(r.text, 'html.parser')
    cancer = soup.find_all('div', class_='article__text')
    all_cancer = []
    for i in cancer:
        all_cancer.append(i.text)
    return all_cancer

def leo(url_5):
    r = requests.get(url_5)
    soup = b(r.text, 'html.parser')
    leo = soup.find_all('div', class_='article__text')
    all_leo = []
    for i in leo:
        all_leo.append(i.text)
    return all_leo

def virgo(url_6):
    r = requests.get(url_6)
    soup = b(r.text, 'html.parser')
    virgo = soup.find_all('div', class_='article__text')
    all_virgo = []
    for i in virgo:
        all_virgo.append(i.text)
    return all_virgo

def libra(url_7):
    r = requests.get(url_7)
    soup = b(r.text, 'html.parser')
    libra = soup.find_all('div', class_='article__text')
    all_libra = []
    for i in libra:
        all_libra.append(i.text)
    return all_libra

def scorpio(url_8):
    r = requests.get(url_8)
    soup = b(r.text, 'html.parser')
    scorpio = soup.find_all('div', class_='article__text')
    all_scorpio = []
    for i in scorpio:
        all_scorpio.append(i.text)
    return all_scorpio

def sagittarius(url_9):
    r = requests.get(url_9)
    soup = b(r.text, 'html.parser')
    sagittarius = soup.find_all('div', class_='article__text')
    all_sagittarius = []
    for i in sagittarius:
        all_sagittarius.append(i.text)
    return all_sagittarius

def capricorn(url_10):
    r = requests.get(url_10)
    soup = b(r.text, 'html.parser')
    capricorn = soup.find_all('div', class_='article__text')
    all_capricorn = []
    for i in capricorn:
        all_capricorn.append(i.text)
    return all_capricorn

def aquarius(url_11):
    r = requests.get(url_11)
    soup = b(r.text, 'html.parser')
    aquarius = soup.find_all('div', class_='article__text')
    all_aquarius = []
    for i in aquarius:
        all_aquarius.append(i.text)
    return all_aquarius


def pisces(url_12):
    r = requests.get(url_12)
    soup = b(r.text, 'html.parser')
    pisces = soup.find_all('div', class_='article__text')
    all_pisces = []
    for i in pisces:
        all_pisces.append(i.text)
    return all_pisces
