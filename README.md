# Онлайн-обучение
# DRF

## Запуск на выполнение домашней работы

Используется Python 3.12
Описание работ для PyCharm в Windows.

1. Создать и активировать виртуальное окружение.
python -m venv venv
.\venv\Scripts\activate

2. Установить зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt 
или средствами PyCharm.

3. Создать файл .env.
Записать в файл настройки, как в шаблоне .env.sample

4. При необходимости создать миграции:
python manage.py makemigrations
Применить миграции
python manage.py migrate

5. Создать суперпользователя
python manage.py csu

6. Для тестового прогона можно использовать файл test.json и users_test.json:
Уточнить тестовые файлы. Работали на первом уроке, на остальных проверить.
python manage.py loaddata test.json
python manage.py loaddata users_test.json

7. Запустить сервер
python manage.py runserver

### Настройка DRF в Docker

#### Сборка с yaml файлом
Создание образа из Dockerfile:
docker-compose build

с запуском контейнера:
docker-compose up --build

с запуском контейнера в фоновом режиме:
docker-compose up -d --build

Запуск контейнера:
docker-compose up
