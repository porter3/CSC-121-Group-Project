#
# Jacob Porter
# November 20, 2021
# Class Registration - Registration module
#

from student import Student


def login(student_id, s_list):
    valid_credentials = False
    pin = None
    ids = [x[0] for x in s_list]
    pins = [x[1] for x in s_list]
    """
    Search the student IDs - if an ID matches the ID passed into the function, use the current index to grab the
    corresponding password
    """
    for i, j in enumerate(ids):
        if j == student_id:
            pin = pins[i]

    pin_input = input('Please enter your PIN: ')
    if pin_input == pin:
        valid_credentials = True

    return valid_credentials


def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}
    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    # login prompting
    student_id = None
    logged_in = False
    while not logged_in:
        student_id = input('Please enter your student ID: ')
        logged_in = login(student_id, student_list)
        if not logged_in:
            print('ID or PIN incorrect')
        else:
            print('ID and PIN verified')

    student = Student()
    while True:
        choice = input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ')
        if choice < 0 or choice > 4 or not choice.isdigit():
            print('Input must be a numeric value between 0 and 4.')
            continue
        choice_int = int(choice)
        if choice_int == 0:
            print('Session ended.')
            exit(1)
        elif choice_int == 1:
            student.add(student_id, course_roster, course_max_size)



main()
