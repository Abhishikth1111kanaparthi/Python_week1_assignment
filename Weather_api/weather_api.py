import requests
import pandas as pd
from datetime import datetime
import os

def fetch_weather_by_id(city_id: int, api_key: str) -> dict:
    """Fetch weather data from OpenWeatherMap using city ID."""
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}
## using the below function to analyze the raw json data 
def analyze_weather(weather_data: dict) -> str:
    """Analyze weather data and return a summary."""
    if not weather_data or "main" not in weather_data:
        return "No data to analyze."

    temp = weather_data["main"]["temp"]
    wind = weather_data.get("wind", {}).get("speed", 0)
    humidity = weather_data["main"].get("humidity", 0)

    # Temperature analysis
    if temp <= 10:
        summary = "Cold (≤10°C)"
    elif 11 <= temp <= 24:
        summary = "Mild (11–24°C)"
    else:
        summary = "Hot (≥25°C)"

    # Add warnings
    if wind > 10:
        summary += " | High wind alert!"
    if humidity > 80:
        summary += " | Humid conditions!"

    return summary

## using this function to log the data to csv file 
def log_weather_by_id(city_id: int, filename: str, api_key: str):
    """Fetch, analyze, and save weather data with analysis to CSV."""
    weather_data = fetch_weather_by_id(city_id, api_key)
    if not weather_data or "main" not in weather_data:
        print("No weather data available.")
        return

    temp = weather_data["main"]["temp"]
    wind = weather_data["wind"]["speed"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"]
    city_name = weather_data["name"]
    analyzed = analyze_weather(weather_data)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get time stamp 

    new_row = {
        "Timestamp": timestamp,
        "City": city_name,
        "Temperature (°C)": temp,
        "Wind Speed (m/s)": wind,
        "Humidity (%)": humidity,
        "Condition": condition,
        "Analysis": analyzed  # This is the analyzed data
    }

    # Append to file using pandas
    # if file does not exists it creates a new file 
    # if files exists it add to that file 
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(filename, index=False)
    print(f"Weather data for {city_name} (with analysis) saved to '{filename}'.")

if __name__ == "__main__":
    # api_key from  open weather 
    API_KEY = "api_key" # removed the key # u can use ur personal key 
    
    ## using the city id from the city.list json data file from openweather website  
    #CITY_ID = 1277333  # Bangalore
    #CITY_ID = 1275339  # Mumbai
    #CITY_ID = 1264527  # chennai
    #CITY_ID = 1269843  # hyderabad
    #CITY_ID = 1273292  # Delhi
    #CITY_ID = 1259229  # pune
    CITY_ID = 0  #  checking how it handles error 
    FILENAME = "weather_log.csv"
    
    weather_data = fetch_weather_by_id(CITY_ID, API_KEY)
    print(weather_data) # prints raw json data 
    
    log_weather_by_id(CITY_ID, FILENAME, API_KEY)
