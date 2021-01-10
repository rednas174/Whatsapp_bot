FROM balenalib/raspberrypi3-alpine-python:3.7
#FROM python:3.7

RUN pip3 install flask numpy

COPY app.py .
COPY bot bot

CMD [ "python3", "./app.py" ]