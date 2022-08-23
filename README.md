### foodgram-project-react

# Дипломный проект курса "Бэкенд Разработчик" (Яндекс Практикум)

### Описание

Онлайн-сервис и API для него. На этом сервисе пользователи 
могут публиковать рецепты, подписываться на публикации других 
пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.

### Установка

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

Запустите проект:

```
python3 manage.py runserver
```

### Примеры

Зарегистрируйте пользователя.  
Отправьте POST запрос на URL:

```
http://127.0.0.1:8000/api/users/
```

Получите токен.  
Отправьте POST запрос на URL:

```
http://127.0.0.1:8000/api/auth/token/login/
```

Получите сприсок рецептов.
Отправьте GET запрос на URL:

```
http://127.0.0.1:8000/api/recipes/
```

Создайте свой рецепт.
Отправьте Post запрос на URL:

```
http://127.0.0.1:8000/api/recipes/
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
