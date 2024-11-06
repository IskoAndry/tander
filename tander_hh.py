import requests
from bs4 import BeautifulSoup

# URL страницы компании на HH.ru
url = "https://hh.ru/employer/49357?hhtmFrom=vacancy"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}

# Отправка запроса и получение содержимого страницы
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(response)

# Список для хранения данных о вакансиях
vacancies = []

# Поиск блоков вакансий на странице
for vacancy in soup.find_all("a", class_="bloko-link"):
    title = vacancy.get_text()
    
    # Проверка, содержит ли название вакансии слово "аналитик"
    if "аналитик" in title.lower():
        # Получение ссылки на вакансию
        link = vacancy["href"]
        if not link.startswith("http"):
            link = "https://hh.ru" + link
        
        # Добавление данных о вакансии в список
        vacancies.append({"title": title, "link": link})

# Вывод найденных вакансий
for vacancy in vacancies:
    print(f"Название: {vacancy['title']}")
    print(f"Ссылка: {vacancy['link']}")
    print("-" * 40)
