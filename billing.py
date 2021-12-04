# Author: Matthew Prentice
# Date: 12/3/2021
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    # for course <var> in c_rosters keys <iterable>:
    total_hours = 0
    
    for course in c_rosters:
        # for s_id in c_rosters values:
        for s_id in c_rosters[course]:
            if id == s_id:
                hours = c_hours[course]
                total_hours += hours

    cost_per_hour = 225.0 if s_in_state else 850.0
    billing = total_hours * cost_per_hour
    return total_hours, billing


def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    print('Course load:', int(hours), 'credit hours')
    print('Enrollment cost: $' + format(cost, ',.2f'))

