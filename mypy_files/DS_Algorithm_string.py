###############Length of string

# input_string = input('Enter your string :')
# length = 0
#for char in input_string:
#     length += 1
# print(length)
#########using In-built function
# input_string = input('Enter your string :')
# lenth_of_string = len(input_string)
# print(lenth_of_string)

##################count characters in string

# string = 'Askhay shiv123'
# substring = string[1:8]
# substring_2 = string[0:13:2]
# substring_3 = string[-1]
# print(substring, substring_2, substring_3)


#######################Replace first occurance character

######### using In-built function
# string = 'Akshay shiv123'
# modified_string = string.replace('1', '&', 1)
# modified_string_2 = string.replace('a', 'A', 2)
# print(modified_string, modified_string_2)


###################swapping charaters in string

# string = 'Akshay shiv123'
# append_str = '@45wxy'
#
# new_str = string + append_str
# print(new_str)

############################subString Replacement
#
# string = 'Hello Akshay!'
# substring = 'Akshay!'
# new_substring = 'World!!'
#
# new_string = string.replace(substring, new_substring)
# print('string is :', string, '\n' "new String is :", new_string)

######################## Length of longest string in python
# string1 = "akash"
# string2 = "banana"
# string3 = "kiwi"
# string4 = "strawberry"
# string5 = "rohan"
#
# max_length = 0
#
# for l in [string1,string2, string3, string4, string5]:
#     current_len = len(l)
#     if current_len > max_length:
#         max_length = current_len
#
# print("longest length of String is :", max_length)

################# nth index character from string
#
# string = input("Enter the string :")
# index = int(input('Enter the index to find :'))
#
# nth_char = string[index]
# print('the character at index', index, 'is :', nth_char)

##################First last chars swapping

# string = input("Enter the string :")
#
# if len(string) >= 2:
#     swapped_string = string[-1] + string[1:-1] + string[0]
#     print('original string is :', string)
#     print('swapped string :', swapped_string)
# else:
#     print('string has less than 2 characters, please re enter the valid string!!')


############################### Remove odd index values
# string = input("Enter the string :")
#
# modified_string_odd = string[::2]
# # modified_string_even = string[1::2]
#
# print('original string is :', string)
# print('string with odd indexes removed :', modified_string_odd)
# # print('string with even indexes removed :', modified_string_even)
#

################################ Count words in a string
#
# sentense = input('Enter the sentense!')
#
# words = sentense.split()
# word_count = len(words)
#
# print('Enterd sentense is :', sentense)
# print('number of words in sentense :', word_count)

###################################### Upper lower case of a string
# string = input("Enter the string :")
#
# uppercase_string = string.upper()
# lowercase_string = string.lower()
#
# print('original string is :', string)
# print('uppercase string is :', uppercase_string)
# print('lowercase string is :',lowercase_string)

######################################### Sort unique words alphanumerically
# sentense = input('Enter the sentense! :')
#
# words = sentense.split()
# unique_words = set(words)
#
# sorted_unique_words = sorted(unique_words)
# print('Entered sentense is :', sentense)
# print('words are :', words)
# print('sorted uniquw words :', sorted_unique_words)

################################### Create html from string
# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>HTML from String</title>
# </head>
# <body>
#     <h1>Hello, Akshay!</h1>
# </body>
# </html>
# """
#
# with open("output.html", "w") as file:
#     file.write(html_content)
#     print("HTML content saved to output.html.")

###################################### Insert string in middle of speical chars

# original_string = input('Enter the sentence: ')
# string_to_insert = "handsome"
#
# special_chars = '!@#$%^&*()_+{}:"<>?|~-=[];,.\/'
# if any(char in original_string for char in special_chars):
#     to_be_replaced = original_string.split(special_chars, 1)
#     for char in special_chars:
#         if char in original_string:
#             to_be_replaced = original_string.split(char, 1)
#             break
#     if len(to_be_replaced) == 2:
#         modified_string = f"{to_be_replaced[0]}{string_to_insert}{to_be_replaced[1]}"
#         print('Original string is:', original_string)
#         print('Modified string sentence is:', modified_string)
#     else:
#         print("Special character not found in the original string.")
# else:
#     print("None of the special characters are present in the original string.")

########################################4 Copies of last 2 chars

# string = input('Enter your String :')
# if len(string) >= 2:
#     last_2_chars = string[-2:]
#     result_string = last_2_chars * 4
#     print('original string is :', string)
#     print(' 4 copies of last two string are :', result_string)
# else:
#     print('string should have min 2 characters!!')

########################################### Length of first 3 chars

# string = input('Enter your String :')
# first_3_chars = string[:3]
# lenth_of_3_chars = len(first_3_chars)
#
# print('original string is :', string)
# print('first three characters are :', first_3_chars)
# print('length of first three characters is :', lenth_of_3_chars)

############################################ Last part of string

# string = input('Enter your String :')
# start_index_by_user = int(input('enter index you have to start from :'))
#
# if len(string) >= 1:
#     last_part = string[start_index_by_user:]
#     print('original string is :', string)
#     print('last part of string is :',last_part)
# else:
#     print('string should have at least one character')

###############################################  reverses a string if it's length is a multiple of 4

# string = input('Enter your String :')
#
# if len(string) % 4 == 0:
#     reversed_string = string[::-1]
#     print('original string is :', string)
#     print('reversed string is :', reversed_string)
# else:
#     print('The length of the string is not a multiple of 4.')

################################################ Convert a given string to all uppercase
#
# string = input('Enter your String :')
# uppercase_string = string.upper()
# print('original string is :', string)
# print('uppercased string is :', uppercase_string)
#
################################################ program to sort a string lexicographically
# original_string = input("Enter a string: ")
# sorted_string = ''.join(sorted(original_string))
#
# print("Original string:", original_string)
# print("Lexicographically sorted string:", sorted_string)

########################################### program to remove a newline in Python
# original_string = input("Enter a string: ")
# string_without_newline = original_string.rstrip('\n')
# print("Original string:")
# print(original_string)
# print("\nString without newline characters:")
# print(string_without_newline)

########################################## program to check whether a string starts with specified characters

# original_string = input("Enter a string :")
# specified_chars = input("Enter character to check if its starting or not :")
#
# if original_string.startswith(specified_chars):
#     print('original string starts with specified character', specified_chars)
# else:
#     print("original string doesn't starts with specified_characters")

########################################### program to create a Caesar encryption
# original_text = input("Enter the text to encrypt: ")
# shift_amount = int(input("Enter the shift amount: "))
# encrypted_text = ""
#
# for char in original_text:
#     if char.isalpha():
#         upper = char.isupper()
#         shifted_char = chr((ord(char) - ord('A' if upper else 'a') + shift_amount) % 26 + ord('A' if upper else 'a'))
#         encrypted_text += shifted_char
#     else:
#         encrypted_text += char
#
# print("Original text:", original_text)
# print("Encrypted text:", encrypted_text)
#

##################################### display formatted text (width=50) as output
# original_text = input("enter text for example")
# width = 50
#
# words = original_text.split()
# current_line = ""
#
# for word in words:
#     if len(current_line + word) <= width:
#         current_line += word + " "
#     else:
#         print(current_line.strip())
#         current_line = word + " "
#
# print(current_line.strip())
################################# remove existing indentation from all of the lines in a given text
#
# indented_text = """
#     This is an example text
#     with some indentation.
#         It has nested indentation.
# """
# lines = indented_text.split('\n')
# indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())
# dedented_text = '\n'.join(line[indent:] for line in lines)
# print('Original text :', indented_text)
# print('text after removing indentaion :', dedented_text)

################################### to add a prefix text to all of the lines in a string
# original_text = '''
#     My name is akshay
#     myname is Sandip
#     my name is sachin'''
#
# prefix = input('Enter prefix :')
# lines = original_text.split('\n')
# prefixed_lines = [prefix + line.strip() for line in lines if line.strip()]
# prefixed_text = '\n'.join(prefixed_lines)
# print('originaltext :', original_text)
# print('prefixed text :', prefixed_text)

############################### to set the indentation of the first line
#
# original_text = """
#      My name is akshay
#      myname is Sandip
#      my name is sachin
# """
# indentation = "    "
# lines = original_text.split('\n')
# current_indentation = lines[0][:len(lines[0]) - len(lines[0].lstrip())]
# lines[0] = indentation + lines[0].lstrip()
# for i in range(1, len(lines)):
#     lines[i] = current_indentation + lines[i].lstrip()
# indented_text = '\n'.join(lines)
# print('originaltext :', original_text)
# print('indented text for first line is :', indented_text)

################################################## to print the following floating numbers upto 2 decimal places

# float_n1 = float(input('Enter first float number :'))
# float_n2 = float(input('Enter second float number :'))
#
# float_formatted_n1 = round(float_n1, 2)
# float_formatted_n2 = round(float_n2, 2)
# print('original float numbers were :',float_n1, float_n2)
# print('2 decimal numbers are :', float_formatted_n1, float_formatted_n2)

######################################### print the following floating numbers upto 2 decimal places with a sign
#
# float_n1 = float(input('Enter first float number :'))
# float_n2 = float(input('Enter second float number :'))
#
# float_formatted_n1 = round(float_n1, 2)
# float_formatted_n2 = round(float_n2, 2)
#
# if float_n1 >= 0:
#     sign1 = '+'
# else:
#     sign1 = '-'
#
# if float_n2 >= 0:
#     sign2 = '+'
# else:
#     sign2 = '-'
#
# print('original float numbers were :', float_n1, float_n2)
# print('2 decimal numbers are :', sign1, float_formatted_n1, sign2, float_formatted_n2)
#

##############################  print the following floating numbers with no decimal places
# # Example floating-point numbers
# float_n1 = float(input('Enter first float number :'))
# float_n2 = float(input('Enter second float number :'))
#
# # Convert the numbers to integers
# int_num1 = int(float_n1)
# int_num2 = int(float_n2)
#
# # Print the integers
# print("Original float numbers :", float_n1, float_n2)
# print("with no decimal places:", int_num1, int_num2)

###################################### print the following integers with zeros on the left of specified width
# Example integers
# num1 = int(input('enter the first number :'))
# num2 = int(input('enter the second number :'))
# width = int(input('Enter the width'))
#
# modified_num1 = str(num1).zfill(width)
# modified_num2 = str(num2).zfill(width)
# print('original numbers are :', num1, num2)
# print('modified numbers are :', modified_num1, modified_num2)

############################################ print the following integers with '*' on the right of specified width
#
# num1 = int(input('enter the first number :'))
# num2 = int(input('enter the second number :'))
# width = int(input('Enter the width'))
#
# modified_num1 = str(num1).ljust(width, '*')
# modified_num2 = str(num2).ljust(width, '*')
#
# print('original numbers are :', num1, num2)
# print('modified numbers are :', modified_num1, modified_num2)

######################################### to display a number with a comma separator
# number = int(input('Enter the number :'))
# formatted_number_format = "{:,}".format(number)
#
# print("Original number:", number)
# print("Formatted with format():", formatted_number_format)


######################################to format a number with a percentage

# value = 0.5862
#
# per_value = "{:.2%}".format(value)
# print('Percentage value is :', per_value)

##################################### to display a number in left, right and center aligned of width 10

# number = int(input('Enter the number :'))
# left_alligned = '{:<10}'.format(number)
# right_alligned = '{:>10}'.format(number)
# center_alligned = '{:^10}'.format(number)
#
# print('Original number :')
# print('left alligned number')

############################################ to count occurrences of a substring in a string
# original_string = "hello Akshay, hello python, hello sandip "
#
# substring_to_count = "hello"
# occurrences_count = original_string.count(substring_to_count)
# print("original string is :")
# print('the substring occurs ', occurrences_count, 'in the original string')

############################################## reverse a string
# string = input('Enter the string :')
# reversed_string = string[::-1]
# print('original string is :', string)
# print('reversed string is :', reversed_string)


################################################# reverse words in a string

# sentense = input('Enter the sentense :')
# words = sentense.split()
# reversed_words = reversed(words)
# reversed_sentence = ''.join(reversed_words)
# print('original string :', sentense)
# print('reversed sentense is :', reversed_sentence)

################################################ strip a set of characters from a string
# string = input('enter the string :')
# chars_to_strip = input('enter the characters which to strip')
#
# stripped_chars = string.strip(chars_to_strip)
# print('Original string :', string)
# print('Striped String :', stripped_chars)
#
# ################################## count repeated characters in a string
#
# string = input('Enter a string :')
# char_count = {}
# for char in string:
#     char = char.lower()
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print('Original string :', string)
# print('repeated charaacters :', char_count)

#################################  square and cube symbol in the area of a rectangle and volume of a cylinder

# length = float(input('Enter length :'))
# width = float(input('Enter width :'))
#
# radius = float(input('Enter radius :'))
# height = float(input('Enter height :'))
#
# area_of_rectangle = length * width
#
# volume_of_cylinder = 3.14 * (radius ** 2) * height
#
# print('area of rectangle is :', area_of_rectangle)
# print('volume of cylinder is :', volume_of_cylinder)

########################################## print the index of the character in a string
# string = input('enter string :')
# for index, char in enumerate(string):
#     print('character',char, 'at index',index)

################################### check if a string contains all letters of the alphabet

# string = input('Enter the string :')
# cleaned_string = ''.join(char.lower() for char in string if char.isalpha())
# contains_all_letters = set(cleaned_string) == set('abcdefghijklmnopqrstuvwxyz')
#
# if contains_all_letters:
#     print('The string contains all letters')
# else:
#     print('The string does not contain all letters')

######################################### convert string to list
# string = input('enter string')
# lst = list(string)
# print('original string :',string, 'type :', type(string))
# print('list converted :',lst, 'type :', type(lst))

####################################### lowercase first n characters in a string

# string = input('enter string :')
# n = int(input('Enter the number of chars to convert in string :'))
# result_string = string[:n].lower() + string[n:]
#
# print('original string :', string)
# print('characters in lowercase :', result_string)

######################################## swap comma and dot in a string
# string = input('enter string :')
# swapped_string = string.replace('.', '_').replace(',', '.').replace('_', ',')
# print('original string :', string)
# print('swapped comma and dot :', swapped_string)

######################################## count and display the vowels of a given text

# text = input('enter text :')
# lower_text = text.lower()
# vowels = 'aeiou'
#
# a_count = e_count = i_count = o_count = u_count = 0
#
# for char in lower_text:
#     if char == 'a':
#         a_count += 1
#     elif char == 'e':
#         e_count += 1
#     elif char == 'i':
#         i_count += 1
#     elif char == 'o':
#         o_count += 1
#     elif char == 'u':
#         u_count += 1
#
# print('original text :')
# print('vowels count  ', '\n\ta:', a_count, '\n\te:', e_count, '\n\ti:', i_count, '\n\to:', o_count, '\n\tu:', u_count,)
#
##################################### split a string on the last occurrence of the delimiter

# input_string = "apple,banana,orange,grape"
#
# delimiter = ","
#
# result = input_string.rsplit(delimiter, 1)
#
# print("Original string:", input_string)
# print("Split result:", result)

######################################## find the first non-repeating character in given string
#
# input_string = "hello, world"
#
# char_counts = {}
#
# for char in input_string:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#         char_counts[char] = 1
#
# first_non_repeating_char = None
# for char in input_string:
#     if char_counts[char] == 1:
#         first_non_repeating_char = char
#         break
# print("Original string :", input_string)
# if first_non_repeating_char:
#     print("First non-repeating character :", first_non_repeating_char)
# else:
#     print("No non-repeating characters found.")

########################################## print all permutations with given repetition number of given string

# input_string = "abc"
# repetition = 3
#
# print("All permutations with repetition :",repetition, input_string)
# for char1 in input_string:
#     for char2 in input_string:
#         if repetition == 2:
#             print(char1 + char2)
#         else:
#             for char3 in input_string:
#                 print(char1 + char2 + char3)

###################################### find the first repeated character in a given string

# input_string = input('enter string')
# seen_chars = set()
# for char in input_string:
#     if char in seen_chars:
#         first_repeated_char = char
#         break
#     seen_chars.add(char)
#
# print("Original string:", input_string)
# if 'first_repeated_char' in locals():
#     print("First repeated character:", first_repeated_char)
# else:
#     print("No repeated characters found.")

########################################## find the first repeated character of a given string where the index of first occurrence is smallest


# input_string = "abacabad"
# char_indices = {}
#
# first_repeated_char = None
# first_repeated_index = float('inf')
#
# for index, char in enumerate(input_string):
#     if char in char_indices:
#         if char_indices[char] < first_repeated_index:
#             first_repeated_char = char
#             first_repeated_index = char_indices[char]
#     else:
#         char_indices[char] = index
#
# print("Original string:", input_string)
# if first_repeated_char is not None:
#     print("First repeated character:", first_repeated_char)
#     print("Index of first occurrence:", first_repeated_index)
# else:
#     print("No repeated characters found.")

################################### find the first repeated word in a given string
#
# input_string = input('Enter String :')
#
# words = input_string.split()
#
# seen_words = set()
#
# first_repeated_word = None
# for word in words:
#     if word in seen_words:
#         first_repeated_word = word
#         break
#     seen_words.add(word)
#
# print("Original string:", input_string)
# if first_repeated_word is not None:
#     print("First repeated word:", first_repeated_word)
# else:
#     print("No repeated words found.")

#######################################  find the second most repeated word in a given string

# string = input('enter string :')
# words = string.split()
#
# words = string.split()
#
# word_counts = {word: words.count(word) for word in set(words)}
#
# second_most_repeated_word = sorted(word_counts, key=word_counts.get, reverse=True)[1] if len(word_counts) > 1 else None
#
#
# print("Original string:", string)
# print("Second most repeated word:", second_most_repeated_word if second_most_repeated_word else "No second most repeated word found.")

########################################## remove spaces from a given string

# string = input('Enter the string :')
# op_string = string.replace(' ', '')
# print('original string :', string)
# print('spaces removed from string :', op_string)

######################################## move spaces to the front of a given string
# string = input('Enter the string :')
# string_with_spaces_at_front = ' ' * string.count(' ') + ''.join(char for char in string if char != ' ')
# print('original string :', string)
# print('String with spaces at the front :',string_with_spaces_at_front)

############################################  find the maximum occurring character in a given string
#
# input_string = input('Enter string :')
#
# characters = []
# counts = []
#
# for char in input_string:
#     if char in characters:
#         index = characters.index(char)
#         counts[index] += 1
#     else:
#         characters.append(char)
#         counts.append(1)
#
# max_occurred_char_index = counts.index(max(counts))
# max_occurred_char = characters[max_occurred_char_index]
#
# print("Original string:", input_string)
# print("Maximum occurring character:", max_occurred_char)

#################################################### capitalize first and last letters of each word of a given string

# input_string = input('enter sentense :')
#
# result_string = ' '.join(word[:-1].capitalize() + word[-1].upper()
#                          if len(word) > 1
#                          else word.capitalize()
#                          for word in input_string.split())
#
# print("Original string:", input_string)
# print("Modified string:", result_string)

############################################## remove duplicate characters of a given string

# input_string = input('Enter String :')
#
# unique_characters = []
# for char in input_string:
#     if char not in unique_characters:
#         unique_characters.append(char)
#
# result_string = ''.join(unique_characters)
#
# print("Original string:", input_string)
# print("String without duplicate characters:", result_string)

#################################### compute sum of digits of a given string

# input_string = input('enter string with numbers :')
#
# digit_sum = sum(int(char) for char in input_string if char.isdigit())
#
# print("Original string:", input_string)
# print("Sum of digits:", digit_sum)

######################################### remove leading zeros from an IP address
#
# ip_address = "192.168.001.001"
#
# formatted_ip = '.'.join(str(int(octet)) for octet in ip_address.split('.'))
#
# print("Original IP address:", ip_address)
# print("IP address without leading zeros:", formatted_ip)

############################################# Reverse a given string  Input : "Python"   Output : "nohtyP"

# input_string = input('Enter the string :')
# reversed_string = input_string[::-1]
#
# print("Original string:", input_string)
# print("Reversed string:", reversed_string)

###################################### Reverse each word in given string Input

# input_string = input('Enter string :')
#
# reversed_words = ' '.join(word[::-1] for word in input_string.split())
#
# print("Original string:", input_string)
# print("String with reversed words:", reversed_words)

########################################### Reverse each word and reverse word again. Input


# input_string = "Reverse each word and reverse again"
#
# reversed_words = ' '.join(word[::-1] for word in input_string.split())[::-1]
#
# print("Original string:", input_string)
# print("String with reversed words and reversed again:", reversed_words)

############################################# accepts a string and calculate the number of digits and letters

input_string = input("Enter a string: ")

num_digits = sum(char.isdigit() for char in input_string)
num_letters = sum(char.isalpha() for char in input_string)

print("Original string:", input_string)
print("Number of digits:", num_digits)
print("Number of letters:", num_letters)


