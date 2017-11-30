# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

# - all data in dict
#  "Name" : {"age", ...,  "classes"[...]...}
# - no classes
# - maximum 10 methods
# - each methods should have less that 7 lines of code
#   (does not include script)
# - dump/load data from JSON
# - optparse for CLI

import json

students = []
attendances = [0, 1]
grades = [1, 2, 3, 4, 5, 6]

welcome_text = '\n\tWELCOME TO STUDENTS RESULTS APP!'
menu_text = '\n\nPRESS:\n\t1) to add new student\t2) to add new subject' \
            '\t3) to start lesson\n\t4) to exit\n\n'

start_lesson_text = '\nWHAT DO YOU WANT TO DO:\n\t1) check attendance\n\t2) add grade' \
                    '\n\t3) calculate average grade of student\n\t4) calculate student attendance' \
                    '\n\t5) end lesson\n'


def add_student():
    name = raw_input('\tName: ')
    surname = raw_input('\tSurname: ')
    new_student = {'name': name, 'surname': surname, 'subjects': []}
    students.append(new_student)
    print ('\n\t\tStudent added successfully!')


def add_subject():
    subject_name = raw_input('\tSubject Name: ')
    new_subject = {subject_name: {'grades': [], 'attendance': []}}
    map(lambda student: student['subjects'].append(new_subject), students)
    print ('\n\t\tSubject added successfully!')


def get_subject(name, surname, subject_name):
    student = next(student for student in students
                   if student['name'] == name and student['surname'] == surname)
    return next((subject for subject in student['subjects']
                if subject.keys()[0] == subject_name), None)


def add_grade(subject_name):
    student = get_student()
    if student:
        grade = raw_input("Grade: ")
        if int(grade) in grades:
            subject = get_subject(student['name'], student['surname'], subject_name)
            if subject: subject[subject_name]['grades'].append(int(grade))
        else:
            print ('\n\tWrong grade!')


def current_subject(list_of_dict):
    for idx, subject in enumerate(list_of_dict):
        print ("%s) %s" % (idx + 1, subject.keys()[0]))
    index_of_subject = raw_input()
    return list_of_dict[int(index_of_subject) - 1]


def get_student():
    for idx, student in enumerate(students):
        print ("%s) %s %s" % (idx + 1, student['name'], student['surname']))
    index_of_student = raw_input()
    return students[int(index_of_student) - 1]


def check_attendance(current_subject):
    for student in students:
        successful = False
        while not successful:
            attendance = raw_input("( 1 - present\t0 - absent )\n\t%s %s: \t" % (student['name'], student['surname']))
            if int(attendance) in attendances:
                subject = get_subject(student['name'], student['surname'], current_subject)
                if subject: subject[current_subject]['attendance'].append(attendance)
                successful = True


def average_grade(current_subject):
    student = get_student()
    if student:
        subject = get_subject(student['name'], student['surname'], current_subject)
        if subject:
            grades_of_student = subject[current_subject]['grades']
            average = float(sum(grades_of_student)) / len(grades_of_student)
            print(
                "%s's %s grades: %s \t average: %s" % (student['name'], student['surname'], grades_of_student, average))


def percentage_attendance(current_subject):
    student = get_student()
    if student:
        subject = get_subject(student['name'], student['surname'], current_subject)
        if subject:
            attendance = subject[current_subject]['attendance']
            percentage = 100.0 * attendance.count('1') / len(attendance)
            print(
                "%s's %s attendance: %s %%" % (student['name'], student['surname'], percentage))


# UI functions

def script_lesson(subject):
    while True:
        selected_option = raw_input(start_lesson_text)
        if selected_option == '1':
            check_attendance(subject)
        elif selected_option == '2':
            add_grade(subject)
        elif selected_option == '3':
            average_grade(subject)
        elif selected_option == '4':
            percentage_attendance(subject)
        elif selected_option == '5':
            break


def script_menu():

    while True:
        try:
            selected_option = raw_input(menu_text)

            if selected_option == '1':
                add_student()
            elif selected_option == '2':
                add_subject()
            elif selected_option == '3':
                if not students:
                    print "Add at least one and student!"
                elif not students[0]['subjects']:
                    print "Add at least one and subject!"
                else:
                    print 'Select subject:'
                    subject = current_subject(students[0]['subjects'])
                    subject = subject.keys()[0]
                    script_lesson(subject)

            elif selected_option == '4':
                break
        except ValueError:
            print "Wrong format!"
        except IndexError:
            print "Index or not exist!"
        except ZeroDivisionError:
            print "Add at least one grade/attendance!"


if __name__ == "__main__":
    print welcome_text

    with open('data.json') as data_file:
        students = json.load(data_file)

    script_menu()

    with open('data.json', 'w') as fp:
        json.dump(students, fp)
