From python:3.8.10

WORKDIR /app

RUN pip install django

COPY . /app/

ENV DJANGO_SETTING_MODULE = mysite.settings

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

VOLUME ["/volume/todo"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 

EXPOSE 8000


