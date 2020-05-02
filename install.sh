#!/bin/bash
#Author: Joe Meier a.k.a Jocomol
#Contact: joelmeier08@gmail.com

apt update
apt dist-upgrade -y
apt install python3 python3-pip sqlite3 neofetch figlet -y
echo "Software installed"

#configuring hardware
#ds1820 (Thermometer)
lsmod
modprobe wire
modprobe w1-gpio
modprobe w1-therm
echo "wire" >> /etc/modules

echo "w1-gpio" >> /etc/modules
echo "w1-therm" >> /etc/modules
echo "#1-Wire ds1820" >> /boot/config.txt
echo "dtoverlay=w1-gpio,gpiopin=4" >> /boot/config.txt

#Database

#scrLib
pip3 install -r requirements.txt

echo "triops" > /etc/hostname
