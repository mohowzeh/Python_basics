'''
freeCodeCamp - Python and Django 
READING AND WRITING FILES
See YouTube: https://youtu.be/jBzwzrDvZ18?t=10408

'''


# # open() opens a file
# # r = read, w = write, a = append, r+ = read and write
# # ---
# print() 
# country_file = open('input-countries.txt', 'r')
# print('Is file readable?', country_file.readable()) # check file access
# print('Third country in file is: ', country_file.readlines()[2]) 
# country_file.close()

# print('---')
# country_file = open('input-countries.txt', 'r')
# for country in country_file.readlines():
#     print(country)
# country_file.close()
# # ---

# write to a new file
# you can create new text files, but also new .py files
# ---
my_list = ['Nick', 'Katrien', 'Elias', 'Leander']
output_file = open('output_file.txt','w')
for i in my_list:
    output_file.write(i)
    output_file.write('\n')
output_file.close()
# ---