from telebot import TeleBot, util
from telebot.types import Message, CallbackQuery

import services as s
from inlineKeyboards import (generate_student_keyboard_markup,
                            generate_university_keyboard_markup)
from local_settings import BOT_API_TOKEN


bot = TeleBot(BOT_API_TOKEN)

help_message = '''
Show command list: /help\n
STUDENTS: /student
    Add new student: /student_create
    Update a student: /student_update
    Deleted a student from list: /student_delete
    Restore a student from deleted list: /student_restore
    Deleted student list: /deleted_students
    Filtered list of students by arrival time: /filter_arrival
    Filtered list of students by university: /filter_university
    Filtered list of students by direction: /filter_direction\n
UNIVERSITY: /university
    View all universities: /university_list
    Create new university: /university_create {Name of University}
    Delete university: /university_delete {Name of University}
'''


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    '''The first and help message'''
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['university'])
def send_welcome(message: Message):
    '''Message with keyboard markup about universities'''
    bot.send_message(message.chat.id, 'Select what you want to do:', reply_markup=generate_university_keyboard_markup())


@bot.message_handler(commands=['student'])
def send_welcome(message: Message):
    '''Message with keyboard markup about students'''
    bot.send_message(message.chat.id, 'Select what you want to do:', reply_markup=generate_student_keyboard_markup())


@bot.message_handler(commands=['university_list'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_list')
def show_universities(data: Message|CallbackQuery):
    '''Show all universities'''
    s.university_list(bot=bot, chat_id=s.get_chat_id_by_type(data))


@bot.message_handler(commands=['university_create'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_create')
def create_university(data: Message|CallbackQuery):
    '''Create new university'''
    s.order_processing(data, s.university_create)


@bot.message_handler(commands=['university_delete'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_delete')
def delete_university(data: Message|CallbackQuery):
    '''Delete university'''
    s.order_processing(data, s.university_delete)


@bot.message_handler(commands=['student_create'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_create')
def create_university(data: Message|CallbackQuery):
    '''Create new student'''
    s.order_processing(data, s.student_create)


@bot.message_handler(commands=['student_update'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_update')
def create_university(data: Message|CallbackQuery):
    '''Update information about a student'''
    s.order_processing(data, s.get_param_and_value)


@bot.message_handler(commands=['student_delete'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_delete')
def create_university(data: Message|CallbackQuery):
    '''Delete student'''
    s.order_processing(data, s.student_delete)


@bot.message_handler(func=lambda message: True)
def unknown(message: Message):
    '''Answer to unknown message'''
    bot.reply_to(message, "I beg your pardon, I don't know this command.")


if __name__ == "__main__":
    bot.polling()