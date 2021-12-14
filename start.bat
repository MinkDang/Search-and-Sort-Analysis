@echo off
py -m pip install -r requirements.txt  --user
cls
set /p Version=What FILE are you running (case sensitive)? 
py %Version%.py