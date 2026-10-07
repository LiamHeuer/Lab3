import requests

HEADERS = {"User-Agent": "WeatherApp (HeuerL@etsu.edu)"}

#any cities can be added to the list by just looking up it's coordinates and adding it here
CITIES = {
    "new york": (40.7128, -74.0060),
    "chicago": (41.8781, -87.6298),
    "los angeles": (34.0522, -118.2437),
    "miami": (25.7617, -80.1918),
    "las vegas": (36.1699, -115.1398),
    "kingsport": (36.5484, -82.5618),
    "johnson city": (36.3133, -81.3533),
}

# function to get weather forecast for a given latitude and longitude from National Weather API
def get_weather(lat, lon):
    # API call 1: turn lat/lon into a forecast URL for grid square
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    points = requests.get(points_url, headers=HEADERS)
    points.raise_for_status()
    forecast_url = points.json()["properties"]["forecast"]
 
    # API call 2: get the forecast
    forecast = requests.get(forecast_url, headers=HEADERS)
    forecast.raise_for_status()
    return forecast.json()["properties"]["periods"]

def main():
    #loop main for wrong inputs and in case they want to ask another city's weather
    while True:
        print("Cities:", ", ".join(CITIES))
        city = input("Pick a city or type exit: ").strip().lower()
    
        if city == "exit":
            print("Goodbye!")
            break
    
        if city not in CITIES:
            print("City not in the list. Try again.")
            continue
    
        lat, lon = CITIES[city]
    
        try:
            periods = get_weather(lat, lon)
        except requests.RequestException as error:
            print("Could not get weather:", error)
            return
    
        print(f"\nWeather for {city.title()}:\n")
        for p in periods[:3]:
            print(f"{p['name']}: {p['temperature']}°{p['temperatureUnit']}, {p['shortForecast']}")

main()