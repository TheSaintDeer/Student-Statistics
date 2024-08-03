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
    Filtered list of students by direction: /filter_direction
    Assign a university to a student: /student_assign
    Working with students at this stage: /student_stage\n
UNIVERSITY: /university
    View all universities: /university_list
    Create new university: /university_create
    Delete university: /university_delete
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
    s.university_list(bot, s.get_chat_id_by_type(data))


@bot.message_handler(commands=['university_create'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_create')
def create_university(data: Message|CallbackQuery):
    '''Create new university'''
    s.order_processing(bot, data, s.university_create)


@bot.message_handler(commands=['university_delete'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'university_delete')
def delete_university(data: Message|CallbackQuery):
    '''Delete university'''
    s.order_processing(bot, data, s.university_delete)


@bot.message_handler(commands=['student_create'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_create')
def create_student(data: Message|CallbackQuery):
    '''Create new student'''
    s.order_processing(bot, data, s.student_create)


@bot.message_handler(commands=['student_update'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_update')
def update_student(data: Message|CallbackQuery):
    '''Update information about a student'''
    s.order_processing(bot, data, s.get_param_and_value)


@bot.message_handler(commands=['student_delete'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_delete')
def delete_student(data: Message|CallbackQuery):
    '''Delete student'''
    s.order_processing(bot, data, s.student_delete)


@bot.message_handler(commands=['student_restore'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_restore')
def restore_student(data: Message|CallbackQuery):
    '''Restore student'''
    s.order_processing(bot, data, s.student_restore)


@bot.message_handler(commands=['deleted_students'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'deleted_students')
def list_deleted_stidents(data: Message|CallbackQuery):
    '''List of deleted students'''
    s.deleted_students(bot, s.get_chat_id_by_type(data))


@bot.message_handler(commands=['filter_arrival'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'filter_arrival')
def filter_by_arrival(data: Message|CallbackQuery):
    '''List of filtered students by arrival time'''

    text = '''
Enter start time and end time in format:\n
    {start_time} - {end_time}
Example:
    2024-07-01 - 2024-09-30
'''
    s.get_params_for_filtering(bot, data, text, s.filter_arrival)

@bot.message_handler(commands=['filter_university'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'filter_university')
def filter_by_university(data: Message|CallbackQuery):
    '''List of filtered students by university'''

    text = '''
        Enter the name of the university:
    '''
    s.get_params_for_filtering(bot, data, text, s.filter_university)


@bot.message_handler(commands=['filter_direction'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'filter_direction')
def filter_by_direction(data: Message|CallbackQuery):
    '''List of filtered students by direction'''

    text = '''
    Enter the name of the direction:\n
List of all directions: Technical, IT, Humanitarian, Creative, Economic, Natural science
'''
    s.get_params_for_filtering(bot, data, text, s.filter_direction)


@bot.message_handler(commands=['student_assign'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_assign')
def assign_student_to_university(data: Message|CallbackQuery):
    '''Link a student to a specific university to show their selected university'''
    s.get_info_for_assing(bot, data)


@bot.message_handler(commands=['student_stage'])
@bot.callback_query_handler(func=lambda callback: callback.data == 'student_stage')
def show_stage_of_student(data: Message|CallbackQuery):
    '''Link a student to a specific university to show their selected university'''
    s.order_processing(bot, data, s.student_stage)


@bot.message_handler(func=lambda message: True)
def unknown(message: Message):
    '''Answer to unknown message'''
    bot.reply_to(message, "I beg your pardon, I don't know this command.")


if __name__ == "__main__":
    bot.polling()