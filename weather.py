import os
import sys
import requests
from dotenv import load_dotenv


def read_config_file(key_name: str) -> str:
    """
    Функция для загрузки ключа API из .env.
    Если ключ найден - возвращается строка, если нет: функция вернет ошибку.
    """

    load_dotenv()
    api_key = os.getenv(key_name)

    if api_key is None:
        raise ValueError(f"Произошла ошибка: {key_name} отсутствует в файле .env")

    return api_key


def return_weather(city: str) -> str:
    """
    Функция делает запрос на получение данных о погоде в городе,
    переданном аргументом в консоль.

    В консоль выводится: текущая температура в градусах Цельсия и текстовое описание погоды.
    Если город не найден, функция вернет ошибку.
    """

    # Получение ключа
    api_key = read_config_file('API_KEY')

    # Формируем url
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        # Отправляем запрос
        response = requests.get(url, params, timeout=10)

        # Проверяем статус http-ответа
        response.raise_for_status()

        # Извлекаем данные из JSON-ответа
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        return f'В городе {city} сегодня {temperature}°C, {description}'

    except requests.exceptions.ConnectionError as e:
        return f'Ошибка подключения к интернету: {e}'

    except requests.exceptions.HTTPError as e:
        if e.response.status_code in (400, 404):
            return f"Ошибка: Город {city} не найден."
        return f"Ошибка API: {e}"

    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"


def input_validation() -> str:
    """
    Функция для проверки ввел ли пользователь город,
    а также корректность введенной строки.

    В случае некорректного ввода или его отсутствия
    функция завершает работу с кодом ошибки.
    """
    if len(sys.argv) < 2:
        print("Ошибка: вы не указали город.\n"
              "Пример ввода: python weather.py Moscow")
        sys.exit(1)

    return sys.argv[1]


# Запуск скрипта
if __name__ == "__main__":
    inp = input_validation()
    result = return_weather(inp)
    print(result)




