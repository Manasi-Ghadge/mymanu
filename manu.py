import requests

# Your API key
API_KEY = 'e67673754678cff2683d18f6d393f1da'

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Location you want to check the weather for
CITY = "London"
COUNTRY_CODE = "GB"

# Construct the final URL
url = f"{BASE_URL}q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric"

# Send GET request to the API
response = requests.get(url)

# If the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Extract weather information
    main = data['main']
    weather = data['weather'][0]
    wind = data['wind']

    # Output the weather information
    print(f"City: {CITY}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Weather: {weather['description']}")
    print(f"Humidity: {main['humidity']}%")
    print(f"Wind Speed: {wind['speed']} m/s")
else:
    print("City not found or error occurred!")