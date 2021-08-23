'''
PYTHON BASICS 
* INPUT/OUTPUT FUNCTIONS: print(), input()
* VARIABLES
* DATA TYPES: string
* STRING MANIPULATION: concatenation, escape characters
* DATA TYPES: integers
* DATA TYPE CONVERSION: str(), int(), bin()
* MATH OPERATORS: +, -, *, /, %
* MATH FUNCTIONS: abs(), round(), max(), min()
* GET USER INPUT FROM CONSOLE
* LISTS
* LISTS - CONCATENATE, REMOVE ENTRIES
* LISTS - DUPLICATE, SORT, POP, DEL
* TUPLES
* FUNCTIONS
* DICTIONARIES
* 2-D LISTS
* IF..THEN..ELSE
* FOR AND IF
* WHILE LOOP
* FOR LOOP 


(a) freeCodeCamp  

YouTube: https://youtu.be/jBzwzrDvZ18

'''

'''
This file comprises different small exercises. 
Each exercise is preceded by a comment line as follows: # ---
Each exercise is closed off by a comment line as follows: # ---
Uncomment one block of code to test it. 
'''

'''
useful editor commands in Visual Studio Code
CTRL + : comments out a block of lines

useful bash terminal commands
clear : clear the terminal screen

useful Python tips:
Single and double quotes around strings have the same functionality
'''


'''INPUT/OUTPUT FUNCTIONS: print(), input()
'''
# ---
# print("Welcome!")
# print('Welcome!')
# 
## printing multiple things at once
# print('This is', 'a sentence.')
## Note: no need to leave a space at the end of a string when a number value follows it
# print("Hello, world! My name is Nick. My age is", 49)
## ---



'''DATA TYPES: string
'''
# ---
# # String is anything between single or double quotes
# print('This is a string.')
# 
# # Strings can be concatenated in print()
# print('This'+' is'+' a'+' string')
# ---



'''STRING MANIPULATION: concatenation, escape characters
'''
## ---
## \ is the escape character for special characters like ' or " or $
## \n is the new line character
## \t is the tab character
## [i] is the position in the string, starting from 0
# 
# sPerson = 'Tim'
# print('Hi ' + sPerson + ',\nhow are you?')
# print('First letter is ' + sPerson[0])
# print('Upper case is ' + sPerson.upper())
# print('Lower case is ' + sPerson.lower())
# print('Is name upper case?', sPerson.isupper())
# print('Length is', len(sPerson))
# print('Index number of letter \'i\' = ', sPerson.index('i'))
# print('Replace letter m by k = ', sPerson.replace('m','k'))
## ---


'''DATA TYPES: numbers
'''
## ---
# iNumber = -6
# fNumber = -6.156
# print(iNumber)
# print(fNumber)
### ---



'''VARIABLES
'''
## ---
# Person = 'Tim'    # string variable
# age = 18  # integer number variable
# print(Person + ' is a boy')   # + sign concatenates strings
# print(Person,'is', age)   # + sign cannot concatenate string and number
# print(Person + ' is from Turkey')
## ---



'''DATA TYPE CONVERSION: str(), int(), bin()
'''
## ---
## str() converts argument to a string 
## bin() converts number to binary string
## int() converts string to integer
# iNumber = -6
# fNumber = -6.156
# newstring = str(iNumber)
# bNumber = bin(iNumber)
# sNumber = '56'
# NumberFromString = int(sNumber)
# print('String: \t' + newstring)
# print('Binary number:\t', bNumber)
# print('Number from string:\t', NumberFromString)



'''MATH OPERATORS: +, -, *, /, %
'''
## ---
# iNumber = -6
# fNumber = -6.156
# print('Add 2:\t\t', iNumber + 2)
# print('Add 3.14:\t', iNumber + 3.14)
# print('Multiply with 2:', iNumber * 2)
# print('Divide by 2:\t', iNumber / 2)
# print('Remainder mod 6:', fNumber%6)
# print('Absolute value: ', abs(fNumber))
# print('Max of 3 numbers:', max(abs(fNumber), 2, 5))
# print('Round decimals:\t', round(fNumber,2))
## ---



'''ADVANCED NUMBERICAL FUNCTIONS
'''
## import math library
## ---
# from math import *
# print('Square root 100 =',sqrt(100))
## ---


'''GET USER INPUT FROM CONSOLE
'''
## ---
# sInputName = input('Give your name: ')
# iAge = int(input('Give your age: '))
# print('We recorded your name as', sInputName, 'and your age as', iAge)
#
## get a phrase and replace one word with another
# sUserSentence = input('Enter your sentence: ')
# print('Your sentence was: \'' + sUserSentence + '\'')
# sOldWord = input('Enter the word to replace: ')
# sNewWord = input('Enter the word to replace it with: ')
# print(sUserSentence.replace(sOldWord, sNewWord))
## ---



'''LISTS
''' 
## lists can be created by using square brackets []
## lists can combine different data types
## negative indexes start at back of list
## ---
# countries = ['UK', 'Belgium', 'Germany', 'Canada', 49]
# print()
# print('List of entries is: ', countries)
# print('Number of entries in list is: ', len(countries))
# print('Fourth entry in list is ' + countries[3])  #index starts from 0
# print('Fourt entry has first letter of ' + countries[3][0])
# print('Entries #2 to end are: ', countries[1:])  #note how '+' does not work
# print('First and second entry in list are ', countries[0:2]) #note how you go one country 'beyond'
# print('Last entry in list is: ', countries[-1])
# print('Second to last entry in list is: ', countries[-2])
# print('type of variable:', type(countries))
# print('data type of the second entry:', type(countries[1]))
# print('data type of the fifth entry:', type(countries[4]))
# print('Is fifth entry an integer?', type(countries[4])==int)
# countries[0] = 'USA'
# print('Newly modified list of entries is: ', countries)
# print()
# 
## lists can be created by using list() constructor 
# countries = list(('UK', 34, False))
# print(countries)
# print(type(countries))
## ---


'''LISTS - CONCATENATE, REMOVE ENTRIES
'''
## concatenate, remove entries
# list1 = [4,3,5,1,2]
# list2 = ['banana', 'apple', 'mango', 'orange']
# print() 
# print('List1 = ', list1)
# print('List2 = ', list2)
# print()
# print('After concatenation: ', list1)
# list2.append('cherry')
# list2.insert(1,'pear')
# print('With added cherry and pear => ', list2)
# list2.remove('banana')
# print('Removed word \'banana\' => ', list2)
# print('Index of mango is: ', list2.index('mango'))
# print('Number of appearances of mango is: ', list2.count('mango'))
# list2.reverse()
# print('Reversed list is: ', list2)
# list2.clear()
# print('After clearing list 2 =>', list2)
# print()
## ---


''' LISTS - DUPLICATE, SORT, POP, DEL
'''
## ---
# list1 = [4,3,5,1,2]
# list2 = ['banana', 'apple']
# print()
# list3 = list1.copy()
# list3.sort()
# print('Copied and sorted list = ', list3)
# list3.pop()
# print('After popping last value =>', list3)
# list3.pop(1)
# print('After popping index 1 =>', list3)
# del list3[1]
# print('After popping index 1 =>', list3)
# del list3  #completely remove list3 (versus clear())
# print('Try to print deleted list => ', list3)
# print()
## ---


'''TUPLES
'''
## tuples are immutable sets of multiple variables
## ---
# my_tuple = (1,2,3,4,1,1,True,'check')
# my_constructor_tuple = tuple((1,2,3))
# print()
# print('Tuple = ', my_tuple)
# print('First entry = ', my_tuple[0])
# print('Type = ', type(my_tuple))
# print('Type of first entry = ', type(my_tuple[0]))
# print('Constructor tuple =', my_constructor_tuple)
# print()
## ---


''' FUNCTIONS
'''
## function basics in Python
## functions need to be both defined and called
## ---
# def greetings_function_1(name1, name2):
#     print('Welcome, ' + str(name1) + ' and ' + str(name2))
# 
# def greetings_function_2(*names):
#     print('Welcome,', names[0])
#     print('Welcome,', names[1])
#     print('Welcome,', names[2])
# 
# def greetings_function_3(name, age):
#     print(name + ', you are ' + str(age) + ' years old.')
# 
# def get_user_input():
#     output_list = list((name,age))
#     
# print()
# greetings_function_1('Nick','Katrien')
# greetings_function_2('Tim', 'John', 'Mary')
# greetings_function_3('John', 48)
# greetings_function_3(name = 'John', age = 48)  #identical as line above
# 
# nameIn = input('Enter your name: ')
# ageIn = input('Enter your age: ')
# greetings_function_3(nameIn,ageIn)
# print()
# 
## return statement
# def add_numbers(num1, num2):
#     return num1+num2
#     print('Hello')  #this line will never be executed
#
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(add_numbers(num1,num2))
## ---



'''DICTIONARIES
'''
# # dictionaries store values in key-value pairs
# # dictionaries do not allow duplicate keys - only last key appearance is stored
# # ---
# my_dict = {
#     'name': 'Tim',  # this will not be stored
#     'name': 'John',
#     'nationality': 'Belgian',
#     'age': 23,
#     'is_Tall': True,
#     'friends': ['Peter', 'Paul', 'Shana']   #you can add lists to dictionairies
# }
# 
# print('Full dictionary:', my_dict)
# print(type(my_dict))
# print('Age is: ', my_dict['age'])
# print(len(my_dict))
# print(my_dict['friends'])
# print(my_dict['friends'][0])    #call one element of the list in the dictionary
# 
# # x = my_dict['name']
# print(x)
# # ---



'''2-D lists
'''
# # ---
# my_2D_list = [
#     [1, 2, 3],
#     [4, 5],
#     [7, 0, -2]
# ]
# print()
# for sublist in my_2D_list:
#     print('Length = ', len(sublist))
#     for j in sublist:
#         print(j)
# print()
# # ---

'''IF..THEN..ELSE
'''
## if .. else .. statement
## ---
# boy = False
# short = True
# if boy==True and short==True:
#     print('He is a short boy.')
# elif boy==True:
#     print('He is a boy.')
# else:
#     print('He is not a short boy.')
## ---


## if .. else .. statement
## ---
# number = int(input('Give a number: '))
# if number%2==0:  
#     print('Number ' + str(number) + ' is an even number.')
# else:
#     print('Number ' + str(number) + ' is an odd number.')
## ---


## if .. else .. statement
## ---
# string1 = 'Tim'
# string2 = 'TIM'
# if string1.upper()==string2.upper(): 
#     print(string1 + ' contains the same letters as ' + string2) 
## ---

'''FOR AND IF
'''
## for and if in Python
## ---
# countries = ['UK', 'Belgium', 'Germany', 'Canada', 49]
# nbrOfIntegers = 0
# for x in countries:
#     if type(x)==int: nbrOfIntegers+=1
# print('Number of integers in list is: ', nbrOfIntegers)
# nbrOfIntegers = 0
## ---


'''WHILE LOOP
'''
# # while loop
# # ---
# i = 1
# while i < 6:
#     print(i)
#     if i == 4: break
#     i += 1
# print('<end>')
# # ---



'''FOR LOOP
'''
# # you can loop through many datatypes, like string, tuples, ...
# # ---
# print()
# for x in range(2,4):
#     print(x)
# else:
#     print('Finished loop.')
# 
# for i in 'Abba':
#     print(i)
# 
# my_list = ['Tim', 'Mary','BREAK', 'Saskia']
# for x in my_list:
#     if x == 'BREAK': break
#     print(x)
# 
# my_tuple = ('Robbie Tuple', 4)
# for x in my_tuple:
#     print(x)
# 
# my_dict = {
#     'name': 'Louis Dictionary', 
#     'age': 48
# }
# for x in my_dict:
#     print(my_dict[x])
# # ---


