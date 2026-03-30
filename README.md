# Weather App

Скрипт для получения текущей погоды через OpenWeatherMap API.

## Установка

1. Клонирование репозитория:
   ```
   git clone <ссылка>
   cd <папка>
   ```

2. Установка зависимостей
    ```
    pip install -r requirements.txt
    ```

3. Создать файл .env по образцу .env.example

4. Вставить API-ключ в .env
   ```
   API_KEY=ваш_ключ
   ```

## Пример использования

```
python weather.py Moscow
```