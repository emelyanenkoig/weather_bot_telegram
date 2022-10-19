import requests
from config import weather_token
from pprint import pprint


def get_weather_geo(lat, lon, weather_token):

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_token}'
        )
        data = r.json()
        pprint(data)

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    lat = input("Введите lat: ")
    lon = input("Введите lon: ")
    get_weather(lat, lon, weather_token)


if __name__ == '__main__':
    main()
