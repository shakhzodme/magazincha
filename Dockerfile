FROM python:latest

WORKDIR /app

RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CMD gunicorn magazincha.wsgi --bind 0.0.0.0:80
CMD python manage.py runserver 0.0.0.0:80