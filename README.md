# django-api-example

***

## Установка

Копируем данный репозиторий и переходим в него:
```
git clone https://github.com/s1veme/django-api-example
cd django-api-example
```

Устанавливаем `virtualenv` и активируем виртуальное окружение: 
```
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
```

Устанавливаем библиотеки: 
```
pip install -r requirements.txt
```

Делаем миграции:
```
python manage.py makemigrations
python manage.py migrate
```

Теперь можно запустить и сам backend:
```
python manage.py runserver
```
