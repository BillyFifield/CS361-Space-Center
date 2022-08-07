from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from wikiscraper.wikiscraper_tools import search_for
import wikipedia
# from flask_mysqldb import MySQL
import os


import json
import sys
import requests

app = Flask(__name__)
CORS(app)

# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs361_fifieldb"
# app.config["MYSQL_PASSWORD"] = "6876"
# app.config["MYSQL_DB"] = "cs361_fifieldb"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# mysql = MySQL(app)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/launch', methods=['GET'])
def launch():
    return render_template('launch.html')

@app.route('/spacecraft', methods=['GET'])
def spacecraft():
    # Gets a wikiscraper search result
    results = search_for('Falcon Heavy')
    print(results['description'])
    newResults = search_for('SpaceX Starship')
    myData = {'Falcon Heavy': {'description': results['description'], 
              'image': results['images'][1]},
              'Starship': {'description': newResults['description'],
              'image': newResults['images'][0]}


             }

    print(myData['Starship']['description'])
    return render_template('spacecraft.j2', data=myData)        
    # search_results = wikipedia.summary('SpaceX Falcon 9')
    # falcon9 = wikipedia.page('SpaceX Falcon 9')
    # content = falcon9.content
    # image = falcon9.images
    
    # print(content)
    # print(image)

    

@app.route('/people', methods=['GET'])
def people():
    return render_template('people.html')

@app.route('/links', methods=['GET'])
def links():
    return render_template('links.html')

@app.route('/launch_craft/<string:craft>', methods=['GET', 'POST'])
def launch_craft(craft):
    craftResults = search_for(craft)
    craftData = {'description': craftResults['description'],
                 'image': craftResults['images'][0],
                 'name': craft
                }
    return render_template('launch_craft.j2', data=craftData)

if __name__ == "__main__":
    app.run(debug=True)