import requests

r = requests.get("https://www.metaweather.com/api/location/28743736")
contents = r.text

print(contents)
