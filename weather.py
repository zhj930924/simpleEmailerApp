import requests

def get_weather_forecast():
    # Connect to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=22903,us&units=imperial&APPID=8c41d93a7030fd24a89875083f02344c'
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    ##print(weather_json)

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    ##print(description)
    temp_min = weather_json['main']['temp_min']
    ##print(temp_min)
    temp_max = weather_json['main']['temp_max']
    ##print(temp_max)

    # Create forecast string
    forecast = 'The CVille forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' F and a low of ' + str(int(temp_min))
    forecast += ' F.'
    return forecast
