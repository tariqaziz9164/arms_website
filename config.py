# config.py

import os

class Config:
    #DEBUG = False
    SECRET_KEY = '12345678'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False