import requests
import json

def get_weather(city):
    """
    Get weather information for a city using OpenWeatherMap API.
    Note: You need to sign up for a free API key at https://openweathermap.org/api
    """
    try:
        # For demo purposes, we'll simulate weather data
        # In a real implementation, you would use an actual API key:
        #
        # API_KEY = "your_api_key_here"
        # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        # response = requests.get(url)
        # data = response.json()
        
        # Simulated weather data for demonstration
        simulated_data = {
            "name": city,
            "main": {
                "temp": 28,
                "humidity": 70
            },
            "weather": [
                {
                    "main": "Clouds",
                    "description": "broken clouds"
                }
            ]
        }
        
        return simulated_data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def umbrella_reminder():
    city = "Hyderabad"
    weather_data = get_weather(city)
    
    if weather_data:
        temp = weather_data["main"]["temp"]
        weather_main = weather_data["weather"][0]["main"]
        weather_desc = weather_data["weather"][0]["description"]
        
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_main} - {weather_desc}")
        
        # Check if umbrella is needed
        rainy_conditions = ["Rain", "Drizzle", "Thunderstorm"]
        if weather_main in rainy_conditions:
            print("\n☂️ UMBRELLA REMINDER: Take an umbrella today!")
            print("It looks like it's going to rain.")
        else:
            print("\nNo need for an umbrella today!")
    else:
        print("Could not retrieve weather information.")

# Run the reminder
if __name__ == "__main__":
    print("Checking weather for umbrella reminder...")
    umbrella_reminder()
    print("\nScript completed.")