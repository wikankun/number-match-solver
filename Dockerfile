FROM python:3.9.6-slim

RUN apt-get update && apt-get install gcc -y && apt-get clean

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 8080
