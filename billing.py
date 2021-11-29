# Author:
# Date:
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, c_rosters, c_hours, s_in_state):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
   for course in c_rosters:
    for s_id in c_rosters[course]:
        if str(id) in s_id:
            # Now what? Should this be wrapped in the for blocks below?

      for ele in s_in_state:
       if s_in_state[ele]:
           # How do I associate the ID to courses and course hours?
           billing = c_hours * float(225.00)
           return c_hours and billing
       if not s_in_state[ele]:
           # How do I associate the ID to courses and course hours?
            billing = c_hours * float(850.00)
            return c_hours and billing


def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    print(str(id), int(hours), float(cost))


