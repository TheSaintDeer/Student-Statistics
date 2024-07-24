import requests

from telebot import TeleBot, util
from telebot.types import Message, CallbackQuery

from local_settings import BASE_URL


def get_chat_id_by_type(data: Message|CallbackQuery) -> int:
    '''Return the chat id depending on whether it is a message 
    or a button click callback.'''

    if type(data) == Message:
        return data.chat.id
    return data.message.chat.id


def university_list(bot: TeleBot, chat_id: int) -> None:
    '''Show all universities'''

    r = requests.get(BASE_URL+'university/')

    if r.status_code == 200:
        universities = '\n'.join(item['name'] for item in r.json())
        for m in util.smart_split(universities, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")

    
def university_create(bot: TeleBot, chat_id: Message, name: str) -> None:
    '''Create new university'''
    
    r = requests.post(BASE_URL+'university/', data={'name': name})

    if r.status_code == 201:
        bot.send_message(chat_id, "The university was created")
    elif r.status_code == 400:
        bot.send_message(chat_id, "A university with that name already exists.")
    else:
        bot.send_message(chat_id, "Uknown problem.")


def university_delete(bot: TeleBot, chat_id: Message, name: str) -> None:
    '''Create new university'''
    
    r = requests.delete(BASE_URL+'university/destroy_by_name/', data={'name': name})
    
    if r.status_code == 204:
        bot.send_message(chat_id, "The university was deleted")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A university with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")