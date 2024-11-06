from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Настройка драйвера для Selenium (замените путь на путь к вашему драйверу)
# driver_path = "C:\\АНДРЕЙ\\Parsing\\chromedriver.exe"  # Укажите путь к драйверу ChromeDriver
driver = webdriver.Chrome()

# URL страницы с вакансиями
url = "https://rabota.magnit.ru/krasnodar/office"
driver.get(url)

try:
    # Ждем, пока элементы вакансий загрузятся
    wait = WebDriverWait(driver, 10)
    vacancies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "office-vacancies__list-item")))
    
    # Список для хранения данных вакансий
    vacancies_data = []
    
    for vacancy in vacancies:
        vacancy_title = vacancy.text.strip()
        vacancy_link = vacancy.get_attribute("href")
        
        # Фильтруем вакансии по ключевому слову "аналитик"
        if "аналитик" in vacancy_title.lower():
            vacancies_data.append({"Название вакансии": vacancy_title, "Ссылка": vacancy_link})
    
    # Запись данных в файл Excel
    if vacancies_data:
        df = pd.DataFrame(vacancies_data)
        df.to_excel("vacancies.xlsx", index=False)
        print("Данные успешно сохранены в файл vacancies.xlsx")
    else:
        print("Вакансий с названием 'аналитик' не найдено.")

finally:
    # Закрываем браузер
    driver.quit()
