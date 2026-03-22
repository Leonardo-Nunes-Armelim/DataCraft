@echo off

REM Activate virtual environment
call .\venv\Scripts\activate.bat

REM Enter the project folder
cd datacraft

REM Run Django server
py manage.py runserver

pause