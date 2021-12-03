@echo off
py -m pip install -r requirements.txt  --user
cls
set /p Version=What VERSION are you running (1 or 2)? 
py Search_v%Version%.py