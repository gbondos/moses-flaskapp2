"""
The config file is going to handle the secret key and the database management
"""
import os #Import to import os
import urllib.parse
username = urllib.parse.quote_plus('gbondos')
password = urllib.parse.quote_plus('Mongo@2020')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    MONGODB_SETTINGS = { 
        'MONGODB_HOST'  :   "mongodb+srv://%s:%s@cluster0-onnfx.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority"%(username, password),
        }