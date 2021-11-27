# ----------------------------------------------------------------
# Author: Robert Puryear
# Date: 11/27/2021
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------
    print("Courses registered:")
    count = 0
    # get the keys / values from c_roster
    for key, value in c_roster.items():
        # if the student id is in a course
        if str(id) in value:
            # increase the total courses count for student
            count += 1
            print(key)
    print(f"Total number: {count}\n")
    return


def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    # adds a student to a course
    course = input("Enter course you want to add: ")
    # get the students registered for the course
    students_in_course = c_roster.get(course)
    # check to see if course is correct
    if course not in c_roster:
        print("Course not found\n")
        return
    # check to see if student already registered for course
    elif str(id) in students_in_course:
        print("You are already enrolled in that course.\n")
        return
    # check if course is full already
    elif len(students_in_course) >= c_max_size.get(course):
        print("Course already full.\n")
        return
    else:
        # add the student ID to the course’s roster and display a message "Course added"
        c_roster[course].append(str(id))
        print("Course added\n")
        return


def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    course = input("Enter course you want to drop: ")
    # get the students registered for the course
    students_in_course = c_roster.get(course)
    # check to see if course is correct
    if course not in c_roster:
        print("Course not found\n")
        return
    # check to see if student already registered for course
    elif str(id) not in students_in_course:
        print("You are not enrolled in that course.\n")
        return
    else:
        # remove student ID from the course’s roster and display a message "Course dropped"
        c_roster[course].remove(str(id))
        print("Course dropped\n")
        return
