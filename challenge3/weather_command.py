from datetime import datetime, timedelta
import requests
import json


city_coords = {
    'galway': ('53.270668', '-9.056790'),
    'oslo': ('59.913868', '10.752245'),
    'london': ('51.507351', '-0.127758')
}

measurements = {
    'temperature': 'temperature_2m_max',
    'rain': 'rain_sum',
    'windspeed': 'windspeed_10m_max'
}

def weather(message):
    message = message.lower()

    # Let's build the API call!

    # For challenge 3.1, you'll need to get the longitude and latitude for Galway
    # and put them in the params below.

    # For 3.2, looks like you'll need a mapping of cities to coordinates. Check out
    # city_coords above, and wire it up to solve this challenge!

    # 3.3 doesn't really introcude any new concepts. You're on your own!

    date_now = (datetime.now() - timedelta(days=-1)).strftime('%Y-%m-%d')
    daily_params = ['temperature_2m_max', 'rain_sum', 'windspeed_10m_max']
    if len(message) != 0:
        temp2 = message.split(' ')
        if len(temp2) == 2:
            town = temp2[0]
            measurement = temp2[1]
            print(town)
            #Our 3.3 part code unfinished
        else:
            temp = city_coords[message]
            params = {
                'latitude': temp[0],  # You need to update this
                'longitude': temp[1], # ... and this
                'start_date': date_now,
                'end_date': date_now,
                'timezone': 'GMT',
                'daily': daily_params
            }        
    else:
        params = {
        'latitude': 53.270668,  # You need to update this
        'longitude': -9.056790, # ... and this
        'start_date': date_now,
        'end_date': date_now,
        'timezone': 'GMT',
        'daily': daily_params
    }

        #Part 3.1 here HINT: INCLUDE PARAMS HERE

    # This makes a request to the weather API with the above info.
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()

    # Let's print the response. Look out for this in your terminal, you'll need to pull
    # out the bits of information that are relevant to the command used.
    print(json.dumps(response, indent=4))

    # This is a placeholder response to show how to drill into the info that you're interested in.
    #return response['temperature_2m_max']['time'][0]
    return response['daily']['time'][0]
    #return response['daily']['time'][0]


