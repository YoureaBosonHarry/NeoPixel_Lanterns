FROM ubuntu:18.04

LABEL maintainer="rath3.14159@protonmail.com"

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get update & apt-get install -y python3-dev python3-pip

RUN apt-get -y update

RUN pip3 install Cython flask rpi_ws281x adafruit-circuitpython-neopixel RPi.GPIO numpy

RUN python3 -m pip install --force-reinstall adafruit-blinka

WORKDIR /NeoPixel_Lanterns

COPY . .

ENTRYPOINT ["python3", "-u", "Server.py"]
