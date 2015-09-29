#!/bin/sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake git pkg-config
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libtesseract-dev
sudo apt-get install libatlas-base-dev gfortran
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install virtualenv virtualenvwrapper
