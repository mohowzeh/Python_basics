'''
freeCodeCamp - Python and Django 
CLASSES AND OBJECTS IN PYTHON
See YouTube: https://youtu.be/jBzwzrDvZ18?t=11803
'''

# import an existing class from another .py file
# ensure the file name does not contain a dash (-) 
# file names with underscores (_) are accepted
from Python_class_Student import Student

print('- - - Now in class inheritance file - - -')

class Person(Student):
    pass

stu1 = Student('Tim', 22,'engineering')
print('The student is ' + stu1.name +
      ', the age is ' + str(stu1.age) + 
      ', and the degree is ' + stu1.degree + '.')

per1 = Person('Katrien', 37, 'literature')
print('The person is ' + per1.name +
      ', the age is ' + str(per1.age) + 
      ', and the degree is ' + per1.degree + '.')

del stu1
del per1
