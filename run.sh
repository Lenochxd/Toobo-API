#!/bin/bash

# Run venv.sh to set up and activate the virtual environment
. ./venv.sh

# Activate the virtual environment
. .venv/bin/activate

# Run main.py
sudo .venv/bin/fastapi run
