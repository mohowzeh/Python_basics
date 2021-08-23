'''
freeCodeCamp - Python and Django 
CLASSES AND OBJECTS IN PYTHON
See YouTube: https://youtu.be/jBzwzrDvZ18?t=11357
'''


# simple class with 2 attributes
# ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

name = input('Enter a name: ')
try:
    age = int(input('Enter an age: '))
except ValueError:
    print('Age should be a number')
    age = 0

person1 = Person(name, age)
print('Person object has name',person1.name,'and age',person1.age)

del person1
# ---


# # use 'pass' in a class when it is as yet undefined
# # this allows further coding
# # ---
# class Person:
#     pass
# # ---



# # simple class
# # ---
# class NvmClass:
#     x = 5

# obj = NvmClass()
# print(obj.x)
# # ---