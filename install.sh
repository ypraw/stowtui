#!/usr/bin/env bash


# init virtual venv
#!/bin/sh
echo -ne '.........   (33%)\r'
printf "Please wait, initializing virtual environtment\n"
sleep 1
python -m venv ./stowtui_venv
source ./stowtui_venv/bin/activate
sleep 1

echo -ne '.........   (66%)\r'
printf "Please wait, installing dependencies\n"
# install all dependecies
pip install -r requirements.txt
clear
sleep 1.5

# run program
echo -ne '.........   (99%)\r'
printf "Please wait, running program"
sleep 1
python -m stowtui