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

import sys
import numpy as np


class Student:

	scores = []
	attendance = []

	def __init__(self, name, surname):
		    self.name = name
		    self.surname = surname
	
	def serializeToJsonFile():
		pass	

	def addNewScore(self, score):
		self.scores.append(score)

	def averageScore(self):
		return np.mean(self.scores)


class GradeBook:
	listOfStudents = []

	def addNewStudent(self, newStudent):
		self.listOfStudents.append(newStudent)

	def removeStudent(self, name, surname):
		self.listOfStudents.remove(Student(name, surname))
	

if __name__ == "__main__":

	gradeBook = GradeBook()

	newStudent = Student("Alex", "Smith")
	newStudent.addNewScore(5)
	newStudent.addNewScore(3)

	gradeBook.addNewStudent(newStudent)

    

