FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /droid_quotator
WORKDIR /droid_quotator
ADD . /droid_quotator/
RUN apt-get -y update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt