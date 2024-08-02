import requests, datetime

from telebot import TeleBot, util
from telebot.types import Message, CallbackQuery

from local_settings import BASE_URL


ID_OF_DIRECTIONS = {
    'Technical': 1,
    'IT': 2,
    'Humanitarian': 3,
    'Creative': 4,
    'Economic': 5,
    'Natural science': 6
}


def get_chat_id_by_type(data: Message|CallbackQuery) -> int:
    '''Return the chat id depending on whether it is a message 
    or a button click callback.'''

    if type(data) == Message:
        return data.chat.id
    return data.message.chat.id

def set_name_and_do_func(message: Message, bot: TeleBot, chat_id: int, func):
    '''Take the entered university name and do certain function'''
    func(bot=bot, chat_id=chat_id, name=message.text)

def get_param_and_value(bot: TeleBot, chat_id: int, name: str):
    '''Get information about the field name and its new value 
    that the user wants to change'''

    text = '''
        Enter field name and new value in format:\n
    Field_Name1 - New_Value1
    Field_Name2 - New_Value2
    '''
    msg = bot.send_message(chat_id, text)
    bot.register_next_step_handler(msg, student_update, bot, chat_id, name)

def order_processing(bot: TeleBot, data: Message|CallbackQuery, func):
    '''Processing a user order'''
    chat_id = get_chat_id_by_type(data)
    msg = bot.send_message(chat_id, "Enter name:")
    bot.register_next_step_handler(msg, set_name_and_do_func, bot, chat_id, func)

def get_params_for_filtering(bot: TeleBot, data: Message|CallbackQuery, text: str, filtering_func):
    '''Get parameters for filtering'''
    chat_id = get_chat_id_by_type(data)
    msg = bot.send_message(chat_id, text)
    bot.register_next_step_handler(msg, filtering_func, bot, chat_id)

def university_list(bot: TeleBot, chat_id: int) -> None:
    '''Show all universities'''

    r = requests.get(BASE_URL+'university/')

    if r.status_code == 200:
        universities = '\n'.join(item['name'] for item in r.json())
        for m in util.smart_split(universities, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")
    
def university_create(bot: TeleBot, chat_id: int, name: str) -> None:
    '''Create new university'''
    
    r = requests.post(BASE_URL+'university/', data={'name': name})

    if r.status_code == 201:
        bot.send_message(chat_id, "The university was created")
    elif r.status_code == 400:
        bot.send_message(chat_id, "A university with that name already exists.")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def university_delete(bot: TeleBot, chat_id: int, name: str) -> None:
    '''Delete university'''
    
    r = requests.delete(BASE_URL+'university/'+name+'/')
    
    if r.status_code == 204:
        bot.send_message(chat_id, "The university was deleted")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A university with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def student_create(bot: TeleBot, chat_id: int, name: str) -> None:
    '''Create new student'''
    
    r = requests.post(BASE_URL+'student/', data={'name': name})

    if r.status_code == 201:
        bot.send_message(chat_id, "The student was created")
    elif r.status_code == 400:
        bot.send_message(chat_id, "A student with that name already exists.")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def student_update(message: Message, bot: TeleBot, chat_id: int, name: str) -> None:
    '''Update student by his name'''

    data = dict(name=name)
    try:
        data.update(dict((k.strip(), v.strip()) for k,v in 
                (item.split(' - ') for item in message.text.split('\n'))))
    except: 
        bot.send_message(chat_id, "Incorrect input format.")
        return
    
    r = requests.put(
        BASE_URL+'student/'+name+'/', 
        data=data
    )

    if r.status_code == 200:
        bot.send_message(chat_id, "The student was updated")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def student_delete(bot: TeleBot, chat_id: int, name: str) -> None:
    '''Delete student by his name'''

    data = dict(name=name, is_deleted=True)
    
    r = requests.put(
        BASE_URL+'student/'+name+'/', 
        data=data
    )
    
    if r.status_code == 200:
        bot.send_message(chat_id, "The student was deleted")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A student with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def student_restore(bot: TeleBot, chat_id: int, name: str) -> None:
    '''Restore student by his name'''

    data = dict(name=name, is_deleted=False)
    
    r = requests.put(
        BASE_URL+'student/'+name+'/', 
        data=data
    )
    
    if r.status_code == 200:
        bot.send_message(chat_id, "The student was restored")
    elif r.status_code == 404:
        bot.send_message(chat_id, "A student with that name wasn't found.")
    else:
        bot.send_message(chat_id, "Uknown problem.")

def deleted_students(bot: TeleBot, chat_id: int) -> None:
    '''Show all universities'''

    r = requests.get(BASE_URL+'student/deleted_students/')

    if r.status_code == 200:
        students = '\n'.join(str(f"{item['name']}({item['adequacy']})") for item in r.json())
        for m in util.smart_split(students, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")

def filter_arrival(message: Message, bot: TeleBot, chat_id: int):
    try:
        start_time, end_time = (param for param in message.text.split(' - '))
    except:
        bot.send_message(chat_id, "Incorrect input format.")
        return

    r = requests.get(BASE_URL+f'student/filter/?start_time={start_time}&end_time={end_time}')

    if r.status_code == 200:
        students = '\n'.join(f"{item['name']}: {item['arrival']}" for item in r.json())
        for m in util.smart_split(students, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")

def filter_university(message: Message, bot: TeleBot, chat_id: int):
    university = message.text
    r = requests.get(BASE_URL+f'student/filter/?university={university}')

    if r.status_code == 200:
        students = '\n'.join(f"{item['name']}: {item['direction']}({item['specialization']})" for item in r.json())
        for m in util.smart_split(students, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")

def filter_direction(message: Message, bot: TeleBot, chat_id: int):
    direction = None
    try:
        direction = ID_OF_DIRECTIONS[message.text]
    except:
        bot.send_message(chat_id, "Uknown direction.")
        
    r = requests.get(BASE_URL+'student/filter/?direction='+str(direction))

    if r.status_code == 200:
        students = '\n'.join(f"{item['name']}: {item['university']}({item['specialization']})" for item in r.json())
        for m in util.smart_split(students, 1000):
            bot.send_message(chat_id, m)
    else:
        bot.send_message(chat_id, "Uknown problem.")

