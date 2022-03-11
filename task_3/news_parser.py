import requests
from bs4 import BeautifulSoup


def get_last_news(source="https://vc.ru"):
    try:
        result = requests.get(source)
    except requests.ConnectionError:
        return f'Ошибка соединения, попробуйте позже или обратитесь к системному администратору'
    except requests.Timeout:
        return f'Превышено время ожиданание ответа, попробуйте позже или обратитесь к системному администратору'
    else:
        soup = BeautifulSoup(result.content, "lxml")
        news = soup.find_all(class_="l-inline")[0]
        text = news.a.text
        return text
