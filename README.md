# Практическая работа 4.6 (HW-04) 
Приложение с рецептами блюд (frontend и backend) с использовнием django, django-rest-framework, react, react-route, swaggerUI.

## Запуск приложения
### Сервер
- установить локальное окружение в директории /server (py -m venv venv)
- активировать локальное окружение (venv/Scripts/activate)
- в дир. /server установить зависимости с помощью команды "pip install -r requirements.txt"
- запустить сервер в дир. /server/recipes с помощью команды "py manage.py runserver"

### Клиент
- установить зависимости в дир. /client/my-app с помощью команды "npm install"
- URL сервера можно установить в index.js (const serverURL)
- для запуска dev-сервера: "npm start"
- для компиляции бандла и запуска на локальном сервере выполнить: npm run build, npm install -g server, serve -s build
- API схема отображается через клиент. Путь: http://localhost:port/api

P.S.
Переход по страницам я реализовал с помощью createBrowserRouter (а не с помощью Switch) как рекомендованно в документации.
Для обновления состояний использовал Route loader: мне показалось это удобней, чем через useState или Redux store

Буду признателен за рекомендации!



