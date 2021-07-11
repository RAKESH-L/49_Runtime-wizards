
import requests
from flask import Flask,render_template
URL = "https://discover.search.hereapi.com/v1/discover"
latitude = 12.96643
longitude = 77.5871
api_key = 'YOUR_API_KEY' 
query = 'bloodbank'
limit = 5

PARAMS = {
            'apikey':api_key,
            'q':query,
            'limit': limit,
            'at':'{},{}'.format(latitude,longitude)
         } 

r = requests.get(url = URL, params = PARAMS) 
data = r.json()


bloodbankOne = data['items'][0]['title']
bloodbankOne_address =  data['items'][0]['address']['label']
bloodbankOne_latitude = data['items'][0]['position']['lat']
bloodbankOne_longitude = data['items'][0]['position']['lng']


bloodbanktwo = data['items'][1]['title']
bloodbanktwo_address =  data['items'][1]['address']['label']
bloodbanktwo_latitude = data['items'][1]['position']['lat']
bloodbanktwo_longitude = data['items'][1]['position']['lng']

bloodbankthree = data['items'][2]['title']
bloodbankthree_address =  data['items'][2]['address']['label']
bloodbankthree_latitude = data['items'][2]['position']['lat']
bloodbankthree_longitude = data['items'][2]['position']['lng']


bloodbankfour = data['items'][3]['title']
bloodbankfour_address =  data['items'][3]['address']['label']
bloodbankfour_latitude = data['items'][3]['position']['lat']
bloodbankfour_longitude = data['items'][3]['position']['lng']

bloodbankfive = data['items'][4]['title']
bloodbankfive_address =  data['items'][4]['address']['label']
bloodbankfive_latitude = data['items'][4]['position']['lat']
bloodbankfive_longitude = data['items'][4]['position']['lng']

app = Flask(__name__)

@app.route('/')

def map_func():
	return render_template('map.html',
                            latitude = latitude,
                            longitude = longitude,
                            apikey=api_key,
                            oneName=bloodbankOne,
                            OneAddress=bloodbankOne_address,
                            oneLatitude=bloodbankOne_latitude,
                            oneLongitude=bloodbankOne_longitude,
                            twoName=bloodbanktwo,
                            twoAddress=bloodbanktwo_address,
                            twoLatitude=bloodbanktwo_latitude,
                            twoLongitude=bloodbanktwo_longitude,
                            threeName=bloodbankthree,
                            threeAddress=bloodbankthree_address,
                            threeLatitude=bloodbankthree_latitude,
                            threeLongitude=bloodbankthree_longitude,
                            fourName=bloodbankfour,		
                            fourAddress=bloodbankfour_address,
                            fourLatitude=bloodbankfour_latitude,
                            fourLongitude=bloodbankfour_longitude,
                            fiveName=bloodbankfive,		
                            fiveAddress=bloodbankfive_address,
                            fiveLatitude=bloodbankfive_latitude,
                            fiveLongitude=bloodbankfive_longitude
                            )

if __name__ == '__main__':
	app.run(debug = False)
