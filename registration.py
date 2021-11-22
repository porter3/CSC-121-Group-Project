#
# Jacob Porter
# November 20, 2021
# Class Registration - Registration module
#

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
    # DELETE
    s_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]

    # student_id = input('Please enter your student ID: ')
    # print(login(student_id, s_list))

    logged_in = False

    while not logged_in:
        student_id = input('Please enter your student ID: ')
        logged_in = login(student_id, s_list)
        if not logged_in:
            print('ID or PIN incorrect')
        else:
            print('ID and PIN verified')


main()
