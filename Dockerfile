FROM balenalib/raspberrypi3-debian:latest

RUN install_packages python3 python3-pip python3-numpy python3-setuptools

RUN pip3 install flask beautifulsoup4 urllib3

COPY app.py .
COPY README.md .
COPY bot bot

CMD [ "python3", "./app.py" ]