import os

from dotenv import load_dotenv

from app import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

if __name__ == '__main__':
    create_app()
