# Rekruto CRUD App

Дефолтная база данных располагается в легковесном файле `db.sqlite3` в корне проекта.

- Используйте `Python 3.9+`
- Создайте виртуальное окружение или используйте окружение текущего пользователя *(не рекомендуется)*
- Установите все необходимые зависимости командой:
`pip install -r requirements.txt`
- Выполняем стартовые миграции:
`python manage.py migrate`
- Локально запускаем проекте:
`python manage.py runserver`
- **Перейдите по ссылке:**
http://127.0.0.1:8000/?name=Rekruto&message=Давай+дружить

> Проект корректно отображает имя и сообщение на индекс-странице, но также можно не передавать параметры в URL при GET-запросе. Реализована кастомная 404 страница с редиректом на индекс для удобства.

## en
Default low-size database file `db.sqlite3` locate in root project folder.

- Use `Python 3.9+` for run this project
- Create virtual environment or use global environment of current user *(not recommended)*
- Install all necessary requirements via command:
`pip install -r requirements.txt`
- Run initial migrations:
`python manage.py migrate`
- Run project locally via command:
`python manage.py runserver`
- **Go to the link:**
http://127.0.0.1:8000/?name=Rekruto&message=Давай+дружить

> The project correctly show name and message on index page, but we also can pass URL params while send GET request. Custom 404 'Not Found' page was made with redirect on index page for more usability.


