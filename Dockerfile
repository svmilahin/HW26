FROM python:3.11-alpine3.17


WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install -r /app/requirements.txt --no-cache-dir

EXPOSE 5000