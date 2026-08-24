from dotenv import load_dotenv
import os
def get_key():
    load_dotenv()
    SECRET_KEY = os.getenv('API_key')
    return SECRET_KEY