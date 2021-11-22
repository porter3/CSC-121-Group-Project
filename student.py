#
# Robert Puryear
# November 13, 2021
# Group Project -  student class
#

class Student:

    # adds a student to a course
    def add_course(id, c_roster, c_max_size):
        while True:
            course = input("Enter course you want to add: ")
            # get the students registered for the course
            students_in_course = c_roster.get(course)
            # check to see if course is correct
            if course not in c_roster:
                print("Course not found")
            # check to see if student already registered for course
            elif str(id) in students_in_course:
                print("You are already enrolled in that course.")
            # check if course is full already
            elif len(students_in_course) >= c_max_size.get(course):
                print("Course already full.")
            else:
                # add the student ID to the course’s roster and display a message "Course added"
                c_roster[course].append(str(id))
                print("Course added")
                break

    def drop_course(id, c_roster):
        while True:
            course = input("Enter course you want to drop: ")
            # get the students registered for the course
            students_in_course = c_roster.get(course)
            # check to see if course is correct
            if course not in c_roster:
                print("Course not found")
            # check to see if student already registered for course
            elif str(id) not in students_in_course:
                print("You are not enrolled in that course.")
            else:
                # remove student ID from the course’s roster and display a message "Course dropped"
                c_roster[course].remove(str(id))
                print("Course dropped")
                break

    def list_courses(id, c_roster):
        print("Courses registered:")
        count = 0
        # get the keys / values from c_roster
        for key, value in c_roster.items():
            # if the student id is in a course
            if str(id) in value:
                # increase the total courses count for student
                count += 1
                print(key)
        print(f"Total number: {count}")
