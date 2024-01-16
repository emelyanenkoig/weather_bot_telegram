import requests
import datetime
from config import weather_token
from pprint import pprint


def get_weather(city, weather_token):

    code_to_smile = {
        'Clear': "Ясно \U00002600",
        'Clouds': "Облачно \U00002601",
        'Rain': "Дождь \U00002614",
        'Drizzle': "Моросня \U00002614",
        'Thunderstorm': "Гроза \U000026A1",
        'Snow':  "Снег \U0001F328",
        'Mist': "Туман \U0001F32B",
        'Fog': "Туман"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&limit={1}&appid={weather_token}&units=metric')
        data = r.json()
        pprint(data)

        # Обработанные данные
        city = data['name']
        curr_temp = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не пойму что там!'


        curr_temp_min = data['main']['temp_min']
        curr_temp_max = data['main']['temp_max']
        curr_wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        print(f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            f"Погода в городе: {city}\nТемпература: {curr_temp} C° {wd}\n"
            f"Мин. Температура: {curr_temp_min}\nМакс. Температура: {curr_temp_max}\n\n"
            f"Скорость ветра: {curr_wind} м/с\n"
            f"Рассвет: {sunrise}\nЗакат: {sunset}\n"
            f"Длительность дня: {length_of_the_day}\n")

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город: ")
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
