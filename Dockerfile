FROM python:3.11

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
