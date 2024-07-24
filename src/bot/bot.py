from telebot import TeleBot, util
from telebot.types import Message, CallbackQuery

import messages as m
import services as s
from inlineKeyboards import (generate_student_keyboard_markup,
                            generate_university_keyboard_markup)
from local_settings import BOT_API_TOKEN


bot = TeleBot(BOT_API_TOKEN)


def set_name_and_do_func(message: Message, chat_id: int, func):
    '''Take the entered university name and do certain function'''

    func(bot=bot, chat_id=chat_id, name=message.text)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    '''The first and help message'''

    bot.send_message(message.chat.id, m.help_message)


@bot.message_handler(commands=['university'])
def send_welcome(message: Message):
    '''The first and help message'''

    bot.send_message(message.chat.id, 'Select what you want to do:', reply_markup=generate_university_keyboard_markup())


@bot.message_handler(commands=['university_list'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_list')
def show_universities(data: Message|CallbackQuery):
    '''Show all universities'''

    s.university_list(bot=bot, chat_id=s.get_chat_id_by_type(data))


@bot.message_handler(commands=['university_create'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_create')
def create_university(data: Message|CallbackQuery):
    '''Create new university'''

    chat_id = s.get_chat_id_by_type(data)
    msg = bot.send_message(chat_id, "Enter university name:")
    bot.register_next_step_handler(msg, set_name_and_do_func, chat_id, s.university_create)


@bot.message_handler(commands=['university_delete'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_delete')
def delete_university(data: Message|CallbackQuery):
    '''Create new university'''

    chat_id = s.get_chat_id_by_type(data)
    msg = bot.send_message(chat_id, "Enter university name:")
    bot.register_next_step_handler(msg, set_name_and_do_func, chat_id, s.university_delete)


if __name__ == "__main__":
    bot.polling()