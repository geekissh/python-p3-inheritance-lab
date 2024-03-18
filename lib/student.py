#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge):
        self.knowledge.append(knowledge)

john_doe_student = Student("John", "Doe")

# Test the learn metho
john_doe_student.learn("I am learning Python")
print(john_doe_student.knowledge)