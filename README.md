#Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, так как у вас не доступа к БД, но можете спокойно использовать код вёрстки или посмотерть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников наша банка.

###Запуск
- Скачайте код
- Создайте файл переменных окружения .env и заполните его следующими данными
```
SECRET_KEY = Ваш секретный ключ
PORT = Номер порта
NAME = Имя базы данных
USER = Логин от вашей учётной записи
PASSWORD = Пароль от учётной записи
HOST = Адрес БД
DEBUG = False (True - при необходимости исправлений ошибок, False - При отсутствии необходимости исправления ошибок)
ALLOWED_HOSTS = [] (Список хостов/доменов, для которых может работать текущий сайт)
```
- Запустите сайт командой:
`python manage.py runserver`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`
###Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).