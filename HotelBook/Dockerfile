# pull official base image
FROM python:3.9.2-alpine
# set work directory
WORKDIR /usr/src/app/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN apk add py-cryptography
RUN apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN pip install cryptography --no-binary cryptography
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .