help_message = '''
Show command list: /help\n
STUDENTS:
    Add new student: /create_stud {Student Full Name}
    Update a student: /update_stud {Student Full Name} {Update Field} {New Value}
    Deleted a student from list: /delete_stud {Student Full Name}
    Restore a student from deleted list: /restore_stud {Student Full Name}
    Deleted student list: /del_stud
    View filtered student list by university or direction: /stud [univ|dir] {Name of Choice}
    Filtered list of students by arrival time: /arrival {MM-YYYY}\n
UNIVERSITY:
    View all universities: /univ
    Add new university: /create_univ {Name of University}
    Delete university: /delete_univ {Name of University}
'''

not_found_command_message = '''
I beg your pardon, I don't know this command. 
'''