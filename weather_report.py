import requests

API_ROOT = "https://www.metaweather.com"
API_LOCATION = "/api/location/search/?query=" # + city
API_WEATHER = "/api/location/" # + woeid

def main():
    try:
        city = ""

        while not city:
            city = input("What city are you in? ")

        location = get_WOEID(city)
        woeid = location[0]["woeid"]

        if len(location) == 0:
            print("Sorry, I don't know where that is. Try with a bigger city. ")
        
        else:
            print(f"Gathering information for {city}")
        
        get_weather_data(woeid)

    except requests.exceptions.ConnectionError:
        print ("Could not connect to the server!")


def get_WOEID(city):

    r = requests.get(API_ROOT + API_LOCATION + city)
    d = r.json()

    return d




# Use WOEID to get weather data
# Convert data from JSON text to Python dictionary

def get_weather_data(woeid):
    try:
        r = requests.get(API_ROOT + API_WEATHER + woeid)
        # Convert the JSON to a Python Dictionary
        d = r.json()

    except requests.exceptions.ConnectionError:
        print ("Could not connect to the server!")


    # Loop over dictionary and display the forecast for each day
    for day in d["consolidated_weather"]:
        date = day["applicable_date"]
        print(f"On {date} the weather will be...")

main()