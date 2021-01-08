FROM balenalib/raspberrypi3-alpine-python:3.7

RUN pip3 install flask

COPY whatsapp_server.py .
COPY command_funcs.py .

CMD [ "python3", "./whatsapp_server.py" ]