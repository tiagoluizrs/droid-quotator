FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install -U pip setuptools
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
ADD . /code/