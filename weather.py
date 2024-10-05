import requests

def get_weather(city_id, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric&lang=he'

    #city = "Haifa"
    #url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            name = data['name']
            weather = data["weather"][0]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            description = weather["description"]

            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather description: {description}")


            weather_info = {
                'temperature': temperature,
                'humidity' : humidity,
                'description': weather["description"],
                'city': name
    }
        else:
            print(f'Returned with error, No weather found!')
    
    except Exception as error:
        print(f'An error occurred while fetching weather data: {error}')

        weather_info = {
        'temperature': 0,
        'description': 'no weather data',
        'city': 'no city name'
        }

    print(f'weather_info: {weather_info}')
    return weather_info
