from requests import get

# The api key of OpenWeatherMap API.
# Can be accuired by visiting openweathermap.org/api
owa_api_key = ''


def get_weather_by_city(city_name: str):
    """
    Get weather info by city
    :param city_name: name of city to get weather of
    :type city_name: str
    :return: JSON object with weather info
    :rtype: JSON object
    """
    response = get('https://api.openweathermap.org/data/2.5/weather', params={'q': city_name, 'APPID': owa_api_key})
    response = get(response.url)

    return response.json()


class Weather:
    name = None
    main = None
    desc = None
    icon = None
    humidity = None
    temp = None
    wind_speed = None
    wind_angle = None

    def __init__(self, city_name):
        json = get_weather_by_city(city_name)

        self.name = json['name']
        self.main = json['weather']['main']
        self.desc = json['weather']['description']
        self.icon = json['weather']['icon']
        self.temp = json['main']['temp']
        self.humidity = json['main']['humidity']

        self.wind_speed = json['wind']['speed']
        self.wind_angle = json['wind']['deg']

    @property
    def image_url(self):
        return 'http://openweathermap.org/img/w/{0}.png'.format(self.icon)
