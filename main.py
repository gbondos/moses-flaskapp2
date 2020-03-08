from flask import Flask 
from config import Config #This imports the Config class from the config.py file
from flask_mongoengine import MongoEngine
# 
# import pymongo
# from pymongo import MongoClient
# import urllib.parse
# username = urllib.parse.quote_plus('gbondos')
# password = urllib.parse.quote_plus('Mongo@2020')

# cluster = MongoClient("mongodb+srv://%s:%s@cluster0-onnfx.mongodb.net/test?retryWrites=true&w=majority"%(username, password))

# db = cluster["UTA_Enrollment"] #Name of database
# User = db["user"] # name of collection
# Course = db["course"]
# Enrollment = db["enrollment"]
####
app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app) #This initialize the mongoengine database
# api.init_app(app)# Initializes the postman api
from routes import * # THis import all the routes files
# users_ = db.user.find({})
# for doc in users_:
#     print(doc)
if __name__ == "__main__":
    app.run(debug = True)