from flask import Flask, render_template
from flask_cors import CORS
from wiki_search import wiki_search
import requests

app = Flask(__name__)
CORS(app)


# Route for the Home Page
@app.route('/', methods=['GET'])
def index():
    API_URL = 'https://api.nasa.gov/planetary/apod?api_key=4uHXJ6jK0bbHUzaAF70DaEfG6mq9uCuLpMNEIt76'
    response = requests.get(API_URL)
    data = response.json()
    if data['media_type'] == 'video':
        potd_data = {
                     'title': data['title'],
                     'url': data['url'],
                     'type': data['media_type'],
                     'description': data['explanation']
                    }
    else:
        potd_data = {
                    'title': data['title'],
                    'description': data['explanation'],
                    'imageURL': data['url'],
                    'copyright': data['copyright']
                    }
    return render_template('index.j2', data=potd_data)



# Route for Launch page to display data for the next 5 launches
@app.route('/launch', methods=['GET'])
def launch():
    API_URL = 'https://fdo.rocketlaunch.live/json/launches/next/5'
    launch_data = get_launch_data(API_URL)    
    return render_template('launch_data.j2', data=launch_data)

def get_flag_data(URL):
    # A method that takes a flag api url as a parameter and returns the image source to 
    # the country flag
    response = requests.get(URL)
    flag = response.text
    return flag

def get_launch_data(URL):
    # A method that takes a launch data api as parameter and returns a json containing information
    # of the next 5 space launches.
    response = requests.get(URL)
    data = response.json()
    l_data = {}
    for i in range(5):
        vehicle = data['result'][i]['vehicle']['name']
        l_data[i] = {'provider': data['result'][i]['provider']['name'],
                     'vehicle_name': vehicle,
                     'mission_name': data['result'][i]['missions'][0]['name'],
                     'mission_desc': data['result'][i]['launch_description'],
                     'weather': data['result'][i]['weather_summary'],
                     'location': data['result'][i]['pad']['location']['name'],
                     'state': data['result'][i]['pad']['location']['statename'],
                     'country': data['result'][i]['pad']['location']['country']
                    }
        v_link = f"localhost:5000/launch_craft/{l_data[i]['provider']} {vehicle}"
        l_data[i]['vehicle_link'] = v_link
        flag_url = f"http://localhost:5353/country/{l_data[i]['country']}"
        flag = get_flag_data(flag_url)
        l_data[i]['flag'] = flag

    return l_data

# Route for the ISS page to display data about the ISS and give it's location
@app.route('/iss', methods=['GET'])
def ISS():

    # Get ISS coordinates from the API
    ISS_URL = 'https://api.wheretheiss.at/v1/satellites/25544'
    iss_data = get_iss_data(ISS_URL)
    
    # Get country and map image of ISS from API
    LOC_URL = f"https://api.wheretheiss.at/v1/coordinates/{iss_data['latitude']},{iss_data['longitude']}"
    loc_data = get_loc_data(LOC_URL)

    return render_template('iss.j2', iss=iss_data, location=loc_data)

def get_iss_data(URL):
    # A method that takes a string of URL for an API and returns the coordiantes and 
    # velocity of the ISS in a json.
    response = requests.get(URL)
    data = response.json()
    velocity = data['velocity']
    velocity = round(velocity, 2)

    iss_data_list = {'latitude': data['latitude'],
                 'longitude': data['longitude'],
                 'altitude': data['altitude'],
                 'velocity': velocity
                }
    return iss_data_list

def get_loc_data(URL):
    # A method that receives a string of a URL for an API and returns the timezone, country, and
    # map of were the ISS is, in json form.
    response = requests.get(URL)
    data = response.json()
    loc_data_list = {'timezone': data['timezone_id'],
                     'country': data['country_code'],
                     'map_url': data['map_url']
                    }
    return loc_data_list


# A route for the People page to display which astronauts are currently in space.
@app.route('/people', methods=['GET'])
def people():
    API_URL = 'http://api.open-notify.org/astros.json'
    response = requests.get(API_URL)
    data = response.json()
    astronautList = data['people']
    count = int(data['number'])
    return render_template('people.j2', data=astronautList, count=count)


#A route for the Launch Craft, which is the craft from the Launch table.
@app.route('/launch_craft/<string:craft>', methods=['GET', 'POST'])
def launch_craft(craft):
    # The method takes a string of a craft from the launch table and sends it to my
    # partner's wiki scraper microservice, which in returns receives an image of the craft
    # and informationa about it.
    craftResults = wiki_search(craft)
    craftData = {'description': craftResults['description'],
                 'image': craftResults['images'][0],
                 'name': craft
                }
    return render_template('launch_craft.j2', data=craftData)


# A route for the Links page which displays different links to difference space organizations.
@app.route('/links', methods=['GET'])
def links():
    links = {
            'nasa': 'https://www.nasa.gov/',
            'spacex': 'https://www.spacex.com/',
            'boeing': 'https://www.boeing.com/space/',
            'lockheed': 'https://www.lockheedmartin.com/en-us/capabilities/space.html',
            'blueorigin': 'https://www.blueorigin.com/',
            'virgin': 'https://www.virgingalactic.com/'
            }
    return render_template('links.j2', data=links)

if __name__ == "__main__":
    app.run(debug=True)
