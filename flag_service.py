# Author: Billy Fifield
# Date: 07/23/2022
# Description: A microservice that listens for a country submitted on PORT 5353, and returns with 
#              an image source that is linked to the country's flag.

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])


@app.route('/country/<string:country>', methods=['GET'])
def get_flag(country):


    # Check to see if United States is properly formatted for the API
    if country == "United States" or country == 'United States of America':
        country = 'USA'

    # If a submitted country has a space, then remove the space to submit it to the API
    for char in country:
        if char == ' ':
            country = country.replace(' ', '', 1)

    flag_api = 'https://countryflagsapi.com/png/'   # Source of the api
    country_url = flag_api + country                # Format the API URL to get the apropriate country flag

    return country_url                              # Return the image source of the country flag

if __name__ == "__main__":
	app.run(host="localhost", port=5353,debug=True)