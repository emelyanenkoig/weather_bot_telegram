import requests
import datetime
from config import bot_token, weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import locale


bot = Bot(token=bot_token)
dp = Dispatcher(bot)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        '🏙 Напишите название <b>городa</b> и я пришлю сводку погоды!\n\n📍 Отправьте <b>геопозицию</b>, а я отправлю вам состояние '
        'погоды!', reply_markup=main_btn(), parse_mode='html')
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['location'])
async def get_weather_geo(message: types.Message):
    code_to_smile = {
        'Clear': "Ясно ☀️",
        'Clouds': "Облачно ⛅️",
        'Rain': "Дождь 🌧",
        'Drizzle': "Моросня 🌧",
        'Thunderstorm': "Гроза ⛈",
        'Snow': "Снег 🌨",
        'Mist': "Туман 🌫",
        'Fog': "Туман 🌫"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={message.location.latitude}&lon={message.location.longitude}&appid={weather_token}&units'
            f'=metric'
        )
        data = r.json()

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
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        length_of_the_day = datetime.datetime.fromtimestamp(
            data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        await message.reply(f"<b>Сегодня</b>:\n"
                            f"{datetime.datetime.now().strftime('%d %B %Y')}\n\n"
                            f"Температура: <b>{curr_temp} C°</b>\n"
                            f"{wd}\n"
                            f"Мин. Температура: {curr_temp_min} C°\nМакс. Температура: {curr_temp_max} C°\n"
                            f"Скорость ветра: {curr_wind} м/с\n\n"
                            f"Рассвет: {sunrise}\nЗакат: {sunset}\n"
                            f"Длительность дня: {length_of_the_day}\n", parse_mode='html')

    except:
        await message.reply("😲 Проверьте название города 😲")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        'Clear': "Ясно ☀️",
        'Clouds': "Облачно ⛅️",
        'Rain': "Дождь 🌧",
        'Drizzle': "Моросня 🌧",
        'Thunderstorm': "Гроза ⛈",
        'Snow': "Снег 🌨",
        'Mist': "Туман 🌫",
        'Fog': "Туман 🌫"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&limit={1}&appid={weather_token}&units'
            f'=metric')
        data = r.json()

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
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        length_of_the_day = datetime.datetime.fromtimestamp(
            data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        await message.reply(f"<b>Сегодня</b>:\n"
                            f"{datetime.datetime.now().strftime('%d %B %Y')}\n\n"
                            f"Температура: <b>{curr_temp} C°</b>\n"
                            f"{wd}\n"
                            f"Мин. Температура: {curr_temp_min} C°\nМакс. Температура: {curr_temp_max} C°\n"
                            f"Скорость ветра: {curr_wind} м/с\n\n"
                            f"Рассвет: {sunrise}\nЗакат: {sunset}\n"
                            f"Длительность дня: {length_of_the_day}\n", parse_mode='html')

    except:
        await message.reply("😲 Проверьте название города 😲")


def main_btn():
    geo = types.KeyboardButton('Геопозиция 📍', request_location=True)
    city = types.KeyboardButton('Москва')
    city2 = types.KeyboardButton('Санкт-Петербург')
    city3 = types.KeyboardButton('Элиста')
    main_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_btn.row(city, city3)
    main_btn.insert(city2)
    main_btn.insert(geo)
    return main_btn


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
