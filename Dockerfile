FROM python3.11.7

ENV PYTHON_VERSION 3.11.7
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=Europe/Moscow

# Установим директорию для работы

WORKDIR /weather_bot_telegram

COPY ./requirements.txt ./

# Устанавливаем зависимости и gunicorn
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r ./requirements.txt

# Копируем файлы и билд
COPY ./ ./

RUN chmod -R 777 ./



