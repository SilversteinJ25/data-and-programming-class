#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:38:51 2024

@author: justinesilverstein
"""
#Silversteinj25

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10,20)
my_instance.x

#2
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10,20)
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.

class Enrolled_classes():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.course = []
    def enroll (self, class_name, course_number, days, times):
        course = [class_name, course_number, days, times]
        self.course.append(course)
        

student1 = Enrolled_classes('Justine Silverstein', 2025)
student1.enroll('Data and Programming: Python', 'PPHA 30537', 'T/TH', '9 to 10:20')
student1.enroll('Legislative Politcs', 'PPHA 30982', 'T/TH', '11-12:20') 
student1.enroll('Higher Ed Policy', 'PPHA 30141', 'M', '9:00-11:50')
student1.course
