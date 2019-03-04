import requests

# try:
#     r = requests.get("https://www.metaweather.com/api/location/2455920")
#     # Convert the JSON to a Python Dictionary
#     d = r.json()

# except requests.exceptions.ConnectionError:
#     print ("Could not connect to the server!")

# for day in d["consolidated_weather"]:
#     date = day["applicable_date"]
#     mintemp = day["min_temp"]
#     humidity = day["humidity"]
#     print(f"The weather on {date} will be:\n"
#             f"Minimum temperature {mintemp}\n"
#             f"Humidity {humidity}\n")


# Ask user what city they are in
# Use city name to get WOEID

def get_WOEID():
    city = input("What city are you in? ")

    try:
        r = requests.get("https://www.metaweather.com/api/location/search/?query=" + city)
        d = r.json()
        woeid = d[0]["woeid"]
        get_weather_data(woeid)

    except requests.exceptions.ConnectionError:
        print ("Could not connect to the server!")


# Use WOEID to get weather data
# Convert data from JSON text to Python dictionary

def get_weather_data(woeid):
    try:
        r = requests.get(f"https://www.metaweather.com/api/location/{woeid}")
        # Convert the JSON to a Python Dictionary
        d = r.json()

    except requests.exceptions.ConnectionError:
        print ("Could not connect to the server!")


    # Loop over dictionary and display the forecast for each day
    for day in d["consolidated_weather"]:
        date = day["applicable_date"]
        print(f"On {date} the weather will be...")

get_WOEID()