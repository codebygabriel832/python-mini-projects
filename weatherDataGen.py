import random
def get_random_weather_data():
    weather_data = {
        'temp' :round(random.uniform(-50, 50)),
        'humidity' : random.randint(0, 100),
        'pressure': random.randint(990, 1011)
    }
    
    weather_data['feels_like'] = round(random.uniform((weather_data['temp'] - 10), (weather_data['temp'] + 10)), 2)
    
    return weather_data
    
    
list = []
for i in range(1, 101):
    list.append(get_random_weather_data())

print(list)
