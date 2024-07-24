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


def set_name_and_do_func(bot: TeleBot, message: Message, chat_id: int, func):
    '''Take the entered university name and do certain function'''
    func(bot=bot, chat_id=chat_id, name=message.text)


def get_param_and_value():
    '''Get information about the field name and its new value 
    that the user wants to change'''
    pass


def order_processing(bot: TeleBot, data: Message|CallbackQuery, func):
    '''Processing a user order'''
    chat_id = get_chat_id_by_type(data)
    msg = bot.send_message(chat_id, "Enter name:")
    bot.register_next_step_handler(msg, set_name_and_do_func, chat_id, func)


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
    '''Delete university'''
    
    r = requests.delete(BASE_URL+'university/destroy_by_name/', data={'name': name})
    
    if r.status_code == 204:
        bot.send_message(chat_id, "The university was deleted")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A university with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")


def student_create(bot: TeleBot, chat_id: Message, name: str) -> None:
    '''Create new student'''
    
    r = requests.post(BASE_URL+'student/', data={'name': name})

    if r.status_code == 201:
        bot.send_message(chat_id, "The student was created")
    elif r.status_code == 400:
        bot.send_message(chat_id, "A student with that name already exists.")
    else:
        bot.send_message(chat_id, "Uknown problem.")


def student_update(bot: TeleBot, chat_id: Message, name: str, param: str, value: str) -> None:
    '''Delete student by his name'''
    
    r = requests.post(
        BASE_URL+'student/update_by_name/', 
        data={
            'name': name,    
            param: value
        }
    )

    if r.status_code == 200:
        bot.send_message(chat_id, "The student was updated")
    else:
        bot.send_message(chat_id, "Uknown problem.")


def student_delete(bot: TeleBot, chat_id: Message, name: str) -> None:
    '''Delete student by his name'''
    
    r = requests.delete(BASE_URL+'student/destroy_by_name/', data={'name': name})
    
    if r.status_code == 204:
        bot.send_message(chat_id, "The student was deleted")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A student with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")