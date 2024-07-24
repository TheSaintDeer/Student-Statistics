from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_student_keyboard_markup():
    kb = InlineKeyboardMarkup()

def generate_university_keyboard_markup():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("University list", callback_data="university_list"),
    )
    kb.add(
        InlineKeyboardButton("Create university", callback_data="university_create"),
        InlineKeyboardButton("Delete university", callback_data="university_delete"),
    )
    return kb