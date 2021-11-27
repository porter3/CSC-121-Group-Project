# ----------------------------------------------------------------
# Author: Jacob Porter, Robert Puryear
# Date: 11/27/2021
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
import student
import billing


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

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

    student_id = input('Enter ID to log in, or 0 to quit: ')

    while student_id != 0:
        logged_in = login(student_id, student_list)
        if not logged_in:
            print('ID or PIN incorrect\n')
            student_id = input('Enter ID to log in, or 0 to quit: ')
        else:
            print('ID and PIN verified\n')
            break

    choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))

    while choice != 0:
        if choice == 1:
            student.add_course(student_id, course_roster, course_max_size)
            choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
        if choice == 2:
            student.drop_course(student_id, course_roster)
            choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))
        if choice == 3:
            student.list_courses(student_id, course_roster)
            choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: "))


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    valid_credentials = False
    pin = None
    ids = [x[0] for x in s_list]
    pins = [x[1] for x in s_list]

    # Search the student IDs - if an ID matches the ID passed into the function, use the current index to grab the
    # corresponding password

    for i, j in enumerate(ids):
        if j == id:
            pin = pins[i]

    pin_input = input('Please enter your PIN: ')
    if pin_input == pin:
        valid_credentials = True

    return valid_credentials


main()
