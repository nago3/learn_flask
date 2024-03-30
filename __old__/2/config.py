import os

from dotenv import load_dotenv

load_dotenv()

HELLO = os.getenv('HELLO')
DEBUG = os.getenv('DEBUG')
