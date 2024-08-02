from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_student_keyboard_markup():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Create sudent", callback_data="student_create"),
        InlineKeyboardButton("Update sudent", callback_data="student_update"),
    )
    kb.add(
        InlineKeyboardButton("Delete sudent", callback_data="student_delete"),
        InlineKeyboardButton("Deleted students", callback_data="deleted_students"),
        InlineKeyboardButton("Restore sudent", callback_data="student_restore"),
    )
    kb.add(
        InlineKeyboardButton("Filter by arrival", callback_data="filter_arrival"),
        InlineKeyboardButton("Filter by university", callback_data="filter_university"),
        InlineKeyboardButton("Filter by direction", callback_data="filter_direction"),
    )
    kb.add(
        InlineKeyboardButton("Assign student", callback_data="student_assign"),
        InlineKeyboardButton("Student stage", callback_data="student_stage"),
    )
    return kb


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