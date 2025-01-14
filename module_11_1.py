            # Домашнее задание по теме "Обзор сторонних библиотек Python"


    # 1. Библиотека `requests`

# Библиотека `requests` предназначена для отправки HTTP-запросов в простой и удобной форме.
                # Она поддерживает различные методы запросов (GET, POST, PUT, DELETE и другие),
                # работу с заголовками, параметрами и куками, а также обработку ответов.

# Пример использования:

import requests

# Отправляем GET-запрос на сайт
response = requests.get('https://api.github.com')

# Проверяем статус ответа
if response.status_code == 200:
    print("Успешно! Данные получены:")
    print(response.json())  # Выводим данные в консоль
else:
    print("Ошибка в запросе:", response.status_code)


# С помощью `requests` я могу легко взаимодействовать с API и получать данные из интернета.
                # Это расширяет возможности Python, позволяя создавать приложения,
                # которые извлекают информацию из внешних источников.


    # 2. Библиотека `pandas`

# Библиотека `pandas` предназначена для работы с данными, обеспечивая структуры данных (DataFrame и Series)
                # для хранения и манипуляции данными. Она предлагает широкий спектр инструментов для анализа данных,
                # работы со временем, фильтрации и агрегации данных.

# Пример использования:

import pandas as pd

# Чтение данных из CSV файла
data = pd.read_csv('C:\\Users\\alexa\\PycharmProjects\\Module_11\\data.csv')

# Вывод первых 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Простая агрегация: среднее значение по колонке 'value'
average_value = data['value'].mean()
print("Среднее значение:", average_value)

# Фильтрация данных: значения больше среднего
filtered_data = data[data['value'] > average_value]
print("Данные выше среднего:")
print(filtered_data)


# Используя `pandas`, я могу эффективно анализировать и манипулировать большими объемами данных.
                # Это особенно полезно для анализа данных в проектах и исследованиях,
                # где требуется быстрая обработка информации.




    # 3. Библиотека `matplotlib`

# Библиотека `matplotlib` предоставляет инструменты для визуализации данных на Python.
                # Она позволяет создавать широкий спектр графиков, от простых линий и столбиков
                # до более сложных визуализаций, таких как 3D-графики.

# Пример использования:

import matplotlib.pyplot as plt

# Данные для визуализации
x = [0, 2, 4, 6, 8, 10]
y = [2, 3, 5, 7, 11, 12]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()


# С помощью `matplotlib` я могу наглядно представить данные,
                # что помогает лучше понять результаты анализа и сделать выводы.
                # Это особенно полезно для презентаций и публикаций, где визуализация данных играет ключевую роль.


# Выбор библиотек `requests`, `pandas` и `matplotlib` существенно расширяет возможности Python.
#                 Каждая из библиотек предоставляет мощные инструменты для работы с данными, анализа и визуализации,
#                 что делает Python более универсальным и эффективным инструментом для разработки и анализа.




