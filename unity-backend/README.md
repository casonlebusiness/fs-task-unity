### Create virtual environment
python3 -m venv env
source env/bin/activate   

### Install requirements
pip install -r requirements.txt

### Run main server
python manage.py runserver

### CELERY SETUP
1. Pull redis docker
2. Run redis server: `docker run --name redis-server -p 6379:6379 -d redis redis-server  --save 60 1 --loglevel warning`
3. Run celery worker: `celery -A unity worker -l INFO`

### Defaults Endpoints
1. Email APIS: http://127.0.0.1:8000/email/api
1. Email reports webapp: http://127.0.0.1:8000/email/reports