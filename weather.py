import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta
import csv
def get_key():
    load_dotenv()
    SECRET_KEY = os.getenv('API_key')
    return SECRET_KEY


    
