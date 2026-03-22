#!/bin/bash

# Activate venv
source venv/bin/activate.ps1

# Enter the project folder
cd datacraft

# Run server
python3 manage.py runserver