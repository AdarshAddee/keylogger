#!/bin/bash

rd="\e[1;31m"
gr="\e[1;32m"
yl="\e[1;33m"

echo -e "${rd}[${gr}!${rd}] ${yl}updating...!"
apt update > /dev/null 2>&1

#echo -e "${rd}[${gr}!${rd}] ${yl}upgrading...!"
#apt upgrade -y > /dev/null 2>&1

echo -e "${rd}[${gr}!${rd}] ${yl}installing requirements...!"
apt install nodejs npm -y > /dev/null 2>&1

echo -e "${rd}[${gr}!${rd}] ${yl}installing dependencies...!"
pip3 install -r requirements.txt > /dev/null 2>&!
npm install > /dev/null 2>&1

echo -e "${rd}[${gr}!${rd}] ${yl}Done...!"
