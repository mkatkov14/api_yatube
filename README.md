# **Api_YAtube**
## API для проекта Yatube ("Социальная сеть блогеров")

### _Технологии_
- Python 3.7
- Django 2.2.19
- DjangoRestFramework 3.12.4
- SQLite
- Pytest

### _Как запустить проект в dev-режиме_
* Сделать Fork репозитория
* Клонировать репозиторий и перейти в него в командной строке:
```
git clone <ссылка_сгенерированная_в_вашем_репозитории>
```
```
cd yatube_final
```
* Создать и активировать виртуальное окружение

для Linux или MacOS:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
для Windows:
```
python -m venv venv
```
```
source venv/Script/activate
```
* Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
* Перейти в папку yatube_api, и выполнить миграции:
```
cd yatube_api
```
```
python3 manage.py migrate
```
* Запустить проект:
```
python3 manage.py runserver
```
_*  в Windows вместо команды "python3" использовать "python"_

---
после запуска проекта, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как должен работать API. Документация представлена в формате Redoc.