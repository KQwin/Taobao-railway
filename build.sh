#!/bin/bash
apt-get update && apt-get install -y wget libnss3 libatk-bridge2.0-0 libxss1 libgtk-3-0 libasound2
pip install -r requirements.txt
playwright install --with-deps chromium
