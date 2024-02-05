# NOTE name need to be Dockerfile
FROM python:3.9

RUN pip install mysql-connector-python
RUN pip install sqlalchemy
RUN pip install pandas

WORKDIR /usr/app/src

COPY main.py ./