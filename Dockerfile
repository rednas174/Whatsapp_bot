FROM balenalib/raspberrypi3-alpine-python:3.7
#FROM python:3.7

RUN apk add -U g++
RUN apk add -U py3-numpy

RUN pip3 install flask

COPY app.py .
COPY bot bot

CMD [ "python3", "./app.py" ]