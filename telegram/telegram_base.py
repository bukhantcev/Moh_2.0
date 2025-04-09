# Используем стандартную библиотеку urllib.request
# для того , чтобы делать запросы.
# Можно использовать сторонние библиотеки requests или httpx
import urllib.request
import json
from forms.models import Event
from django.shortcuts import get_object_or_404
import os
from dotenv import load_dotenv

load_dotenv()

# Тут будет ваш токен, который вы получили при создании бота
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Тут нужно указать название канала в ссылке,которое начинается с @
# Тут я указал для примера созданный канал
# CHAT_ID = "-1002170807806"
CHAT_ID = "404354012"
THREAD_ID = '2'



def send_telegram_message(id, author=''):
    event = get_object_or_404(Event,id=id)
    ev_data = f'{str(event.date).split(" ")[0].split("-")[2]}.{str(event.date).split(" ")[0].split("-")[1]}.{str(event.date).split(" ")[0].split("-")[0]}'
    ev_time = f'{str(event.date).split(" ")[1].split(":")[0]}:{str(event.date).split(" ")[1].split(":")[1]}'
    staff_list = []
    if event.svet == 'Да':
        staff_list.append('Свет')
    if event.zvuk == 'Да':
        staff_list.append('Звук')
    if event.video == 'Да':
        staff_list.append('Видео')
    if event.decor == 'Да':
        staff_list.append('Декорации')
    if event.rekvizit == 'Да':
        staff_list.append('Реквизит')
    if event.grim == 'Да':
        staff_list.append('Грим')
    if event.kostum == 'Да':
        staff_list.append('Костюм')
    ev_staff = '\n'.join(staff_list)
    text = text_message = f'{author}\n\nДата: {ev_data}\n\nВремя: {ev_time}\n\nМесто проведения: {event.location}\n\n{event.type} "{event.name}"\n\nВызываются службы: \n{ev_staff}\n\nОписание: {event.utochneniya}'
    # Используется метод sendMessage API Telegram
    # Обратите внимание , что мы тут используем BOT_TOKEN
    api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    #Указаваем в параметрах CHAT_ID и само сообщение
    # input_data = json.dumps(
    #     {
    #         'chat_id': CHAT_ID,
    #         'message_thread_id' : THREAD_ID,
    #         'text': text,
    #     }
    # ).encode()
    input_data = json.dumps(
        {
            'chat_id': CHAT_ID,
            'text': text,
        }
    ).encode()

    try:
        req = urllib.request.Request(
            url=api_url,
            data=input_data,
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            #Тут выводим ответ
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)





# if __name__ == "__main__":
#     send_telegram_message()

# 404354012