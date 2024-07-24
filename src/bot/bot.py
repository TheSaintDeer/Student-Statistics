import requests

import telebot
from telebot.types import Message

from local_settings import BOT_API_TOKEN, BASE_URL
import messages as m

bot = telebot.TeleBot(BOT_API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    '''The first and help message'''

    bot.send_message(message.chat.id, m.help_message)


@bot.message_handler(commands=['univ'])
def show_university_list(message: Message):
    '''Show the entire list of universities that have a selected direction
      or if the direction is not specified, then show all universities'''
    
    r = requests.get(BASE_URL+'university/')
    print(r.status_code, r.json())

    if r.status_code == 200:
        bot.send_message(message.chat.id, m.print_univ(r.json()))
    else:
        bot.send_message(message.chat.id, "Uknown problem.")


@bot.message_handler(commands=['create_univ'])
def create_university(message: Message):
    '''Create new university'''

    command, *param = message.text.split()

    if not param:
        return bot.send_message(message.chat.id, "You didn't enter name of university.")

    r = requests.post(BASE_URL+'university/', data={'name': param[0]})
    print(r.status_code, r.json())

    if r.status_code == 201:
        bot.send_message(message.chat.id, "The university was created")
    elif r.status_code == 400:
        bot.send_message(message.chat.id, "A university with that name already exists.")
    else:
        bot.send_message(message.chat.id, "Uknown problem.")
    

@bot.message_handler(commands=['delete_univ'])
def delete_university(message: Message):
    '''Delete university'''
    
    command, *param = message.text.split()

    if not param:
        return bot.send_message(message.chat.id, "You didn't enter name of university.")

    r = requests.delete(BASE_URL+'university/destroy_by_name/', data={'name': param[0]})
    print(r.status_code)
    
    if r.status_code == 204:
        bot.send_message(message.chat.id, "The university was deleted")
    elif r.status_code == 404:
        bot.send_message(message.chat.id, "A university with that name wasn't found.")
    else:
        bot.send_message(message.chat.id, "Uknown problem.")


@bot.message_handler(commands=['create_stud'])
def create_student(message: Message):
    '''Create a new student'''

    command, *param = message.text.split()

    if not param:
        return bot.send_message(message.chat.id, "You didn't enter name of student.")

    r = requests.post(BASE_URL+'student/', data={'name': param[0]})
    print(r.status_code, r.json())

    if r.status_code == 201:
        bot.send_message(message.chat.id, "The student was created")
    elif r.status_code == 400:
        bot.send_message(message.chat.id, "A student with that name already exists.")
    else:
        bot.send_message(message.chat.id, "Uknown problem.")


@bot.message_handler(commands=['update_stud'])
def create_student(message: Message):
    '''Update a new student'''

    command, *param = message.text.split()

    if not param:
        return bot.send_message(message.chat.id, "You didn't enter name of student.")

    r = requests.post(BASE_URL+'student/', data={'name': param[0]})
    print(r.status_code, r.json())

    if r.status_code == 201:
        bot.send_message(message.chat.id, "The student was created")
    elif r.status_code == 400:
        bot.send_message(message.chat.id, "A student with that name already exists.")
    else:
        bot.send_message(message.chat.id, "Uknown problem.")


@bot.message_handler(func=lambda message: True)
def unknown(message: Message):
    '''Answer to unknown message'''
    bot.reply_to(message, m.not_found_command_message)


if __name__ == "__main__":
    bot.polling()