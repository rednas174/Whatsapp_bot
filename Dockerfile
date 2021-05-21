# FROM balenalib/raspberrypi3-debian:latest
FROM amd64/ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 python3-pip python3-numpy python3-setuptools -y
RUN pip3 install flask beautifulsoup4 urllib3

ENV TZ=Europe/london

COPY app.py .
COPY README.md .
COPY bot bot

CMD [ "python3", "./app.py" ]
