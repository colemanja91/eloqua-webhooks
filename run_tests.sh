#!/bin/bash

# Run all defined tests

echo "Check if correct packages installed..."
pip install nose
pip install pylint

echo "Set test env vars..."
export WEBHOOK_USR=user
export WEBHOOK_PWD=password

echo "Run nosetests..."
nosetests

echo "Run pylint..."
pylint ./app.py
pylint ./api/
