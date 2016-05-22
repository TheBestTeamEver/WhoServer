# WhoServer

## API
- /api/<номер_уровня>/level/
- /api/all/
- /api/get_top/
- /api/get_random_urls/
- /api/registration/
- /api/authentication/
- /api/upload/

## Разворачивание проекта

### Создание окружения
```
virtualenv venv
cd venv
. bin/activate
git clone https://github.com/TheBestTeamEver/WhoServer.git
cd WhoServer
pip install -r requirements.txt
```
### Создание базы данных
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
