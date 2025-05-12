from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_info = (
            f"City: {city}\n"
            f"Status: {w.detailed_status}\n"
            f"Temp: {w.temperature('celsius')['temp']} °C\n"
            f"Humidity: {w.humidity}%\n"
            f"Wind: {w.wind()['speed']} m/s\n"
            f"Clouds: {w.clouds}%"
        )
    except Exception as e:
        weather_info = f"Error: {e}"
    return weather_info


    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)                  # 75





