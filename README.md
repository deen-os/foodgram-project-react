### foodgram-project-react

# Дипломный проект курса "Бэкенд Разработчик" (Яндекс Практикум)

### Описание

Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

### Запуск проекта на Docker Desktop

Скопируйте проект на свой компьютер:

```
git clone https://github.com/LariosDeen/foodgram-project-react
```

Cоздайте и активируйте виртуальное окружение для этого проекта:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:

```
python3 manage.py migrate
```

Перейдите в директорию проекта:

```
cd backend
```

Создайте файл .env в директории backend и заполните его данными по этому 
образцу:

```
SECRET_KEY='django-insecure-nsxoy+s&z^f(2$vot&-m!3+uacrm1jikv6!mb+ut&*thlrn=m7'
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DEBUG=False
```

Создайте образ backend (текущая директория должна быть backend):

```
docker build -t dimlar/foodgram_backend:latest .
```

Перейдите в директорию infra:

```
cd ../infra
```

Запустите docker-compose:

```
docker-compose up
```

Выполните миграции в контейнере созданном из образа backend:

```
docker-compose exec -T backend python manage.py migrate
```

Загрузите статические файлы в контейнере созданном из образа backend:

```
docker-compose exec -T backend python manage.py collectstatic --no-input
```

Запустите проект в браузере.
Введите в адресную строку браузера:

```
localhost
```

#### В проекте использованы технологии:
* Python
* React
* Django
* Django REST Framework
* Linux
* Docker
* Docker-compose
* Postgres
* Gunicorn
* Nginx
* Workflow

Проект выполнил студент 31 когорты Яндекс Практикума  
Лариос Димитри  
https://github.com/LariosDeen  
https://t.me/dimilari
