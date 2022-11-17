FROM python:3.10-alpine
MAINTAINER mukundchandra15@gmail.com
RUN apt-get update
COPY app .
EXPOSE 5000/tcp
RUN pip install -r requirements.yml
RUN python ./micksapp.py