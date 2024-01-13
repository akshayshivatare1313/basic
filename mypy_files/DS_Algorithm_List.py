####################### Sum of elements

# my_list =[1,2,3,4,5,6,7,8,9]
# sum = 0
#
# for element in my_list:
#     sum += element
# print('sum is :', sum)

################################# Mulitply of elements

# my_list = [2,4,2]
# multipilaction = 1
# for element in my_list:
#     multipilaction *= element
# print('multiplication of elements :', multipilaction)

################################### Largest number from list

# my_list = [2,7,4,9,15,66,82,4,6,99,0,34,41,23]
# largest_num_in_list = 0
#
# for number in my_list:
#     if number > largest_num_in_list:
#         largest_num_in_list = number
#
# print('largest number in list is :', largest_num_in_list)

################################################# Smallest number from list
# my_list = [2,7,4,9,15,66,82,4,6,99,34,41,23]
# smallest_num_in_list = my_list[0]
#
# for number in my_list:
#     if number < smallest_num_in_list:
#         smallest_num_in_list = number
# print('largest number in list is :', smallest_num_in_list)

########################################### Count no of strings whose length is 2

# my_list = ["ab", "cd", "ef", "ghi", "jk, 'lmnop"]
#
# count_of_strings = 0
#
# for string in my_list:
#     if len(string) == 2:
#         count_of_strings += 1
#
# print("Number of strings with length 2:", count_of_strings)

########################################### Sort elements in increasing order

# my_list = [10, 5, 8, 15, 3]
#
# sorted_list = sorted(my_list)
# print("Original list:", my_list)
# print("Sorted list in increasing order:", sorted_list)

########################################## Remove duplicates from list

# my_list = [1, 2, 2, 3, 4, 4, 5]
#
# index = 0
# while index < len(my_list):
#     current_element = my_list[index]
#     if my_list.count(current_element) > 1:
#         my_list.remove(current_element)
#     else:
#         index += 1
# print("List without duplicates:", my_list)

######################################### Check list is empty or not

# my_list = [2, 3]
#
# if not my_list:
#     print("The list is empty.")
# else:
#     print("The list is not empty.")
#
############################################## Clone or copy

# my_list = list(input('Enter the list elements :'))
# copy_list = my_list.copy()
# print('my list is :', my_list)
# print('copied list is :', copy_list)

################################################# Words that are longer than any element

# word_list = ["apple", "banana", "orange", "kiwi", "grape"]
# max_length = max(len(word) for word in word_list)
#
# longer_words = [word for word in word_list if len(word) > max_length]
# print("Words longer than any element :", longer_words)

################################################## Find common element from 2 lists
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = []
# for element in list1 :
#     if element in list2:
#         common_elements.append(element)
#
# print("Common elements :", common_elements)
#
################################################# Remove specified index from list and print

# list1 = [1, 2, 3, 4, 5]
# print('original list :', list1)
# lst = list1.pop(4)
# print('removed element :', lst)
# print('original list after removing index :', list1)
#
############################################## write 3d array
# array_3d = [
#     [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#     ]
#             ]
# print(array_3d)

############################################## Remove even elements and print list

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = 0
# while index < len(mylist):
#     if mylist[index]  % 2 ==0 :
#         mylist.pop(index)
#     else:
#         index += 1
# print('removed even elements from original list :', mylist)

################################################## Shuffle list and print
# import random
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# shuffled_list =  random.shuffle(my_list)
# print('shuffled list :', my_list)

################################################### First,Last elements whose square value is between 1 and 30

# my_list = [1, 2, 3, 6, 7, 8, 9]
#
# first_element, last_element = None, None
#
# for element in my_list:
#     square = element ** 2
#     if 1 <= square <= 30:
#         if first_element is None:
#             first_element = element
#         last_element = element
#
# print("First element:", first_element)
# print("Last element:", last_element)

############################################# First,Last elements whose square value is between 1 and 30,except first 5

# my_list = [1, 2, 3,4, 5, 6, 7, 8, 9,10]
#
# first_element, last_element = None, None
#
# for element in my_list[3:]:
#     square = element ** 2
#     if 1 <= square <= 30:
#         if first_element is None:
#             first_element = element
#         last_element = element
#
# print("First element:", first_element)
# print("Last element:", last_element)

################################################### All permutations of list elements


###################################################### difference between two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# difference1 = list(set(list1) - set(list2))
#
# difference2 = list(set(list2) - set(list1))
#
# print("Difference (list1 - list2):", difference1)
# print("Difference (list2 - list1):", difference2)

################################################# To access index of list
# my_list = [10, 20, 30, 40, 50]
#
# for index  in range(len(my_list)):
#     print('Index :', index )

############################################### # List of characters
# char_list = ['a', 'b', 'c', 'd', 'e']
# result_string = ''.join(char_list)
#
# print("joined  string :", result_string)

############################################### Finding index of an item in specified list
#
# my_list = ['akshay', 'akash', 'priya', 'shubham']
#
# item_to_find = 'priya'
#
# index_of_item = my_list.index(item_to_find)
# print('found item index is :', index_of_item )

############################################## Append a list to second list
#
# lst1 = [1, 'akshay', 9, 'sameer', 6, 97]
# lst2 =[0, 'priya', 4, 'sandy', 673]
# print('list 1 is :', lst1)
# print('list 2 is :', lst2)
# lst2.append(lst1)
# print('list2 after Appending list1 :', lst2)

############################################## Select an item randomly
# import random
#
# lst1 = [1, 'akshay', 9, 'sameer', 6, 97]
# random_itm = random.choice(lst1)
# print('random item chosed is :', random_itm)

#############################################Check circularly identical in two lists
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 1, 2]
#
#
# if len(list1) != len(list2):
#     print("The lists are not circularly identical.")
# else:
#     circular_list = list1 + list1
#     if any(list2 == circular_list[i:i+len(list2)]
#            for i in range(len(list1))):
#         print("The lists are circularly identical.")
#     else:
#         print("The lists are not circularly identical.")
############################################# Finding a second smallest number
# list = [3, 4, 5, 1, 2]
# sorted_list = sorted(list)
# print('the second smallest number is :', sorted_list[1])

############################################## Finding a second largest number
# list = [3, 4, 5, 1, 2]
# sorted_list = sorted(list)
# print('the second largest number is :', sorted_list[-2])

##################################################  get unique values

# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
#
# unique_values = set(my_list)
#
# unique_list = list(unique_values)
# print('original list is :', my_list)
# print('list with unique values :', unique_list)

################################################### Frequency of elements

# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# frequency_dict = {}
#
# for element in my_list:
#     if element in frequency_dict:
#         frequency_dict[element] += 1
#     else:
#         frequency_dict[element] = 1
#
# # Print the result
# print("Original list:", my_list)
# print("Frequency of elements:", frequency_dict)

################################################# Counting number elementswithin a specified ranges


# my_list = [5, 12, 20, 8, 15, 30, 25, 18, 10]
#
# range1 = (0, 10)
# range2 = (10, 20)
# range3 = (20, 30)
#
# count_range1 = sum(range1[0] <= x < range1[1] for x in my_list)
# count_range2 = sum(range2[0] <= x < range2[1] for x in my_list)
# count_range3 = sum(range3[0] <= x < range3[1] for x in my_list)
#
# print("Original list :", my_list)
# print("Number of elements in range o to 10 :", count_range1)
# print("Number of elements in range 11 to 20 :", count_range2)
# print("Number of elements in range 21 to 30 :", count_range3)

################################################## Counting number elementswithin a specified ranges

# my_list = [1, 2, 3, [4, 5], 6, 7, 8]
#
# sublist_to_check = [4, 5, 6]
#
# sublist_found = False
#
# for element in my_list:
#     if isinstance(element, list) and element == sublist_to_check:
#         sublist_found = True
#         break
#
# if sublist_found:
#     print("The list contains the sublist:", sublist_to_check)
# else:
#     print("The list does not contain the sublist:", sublist_to_check)

###########################################
# my_list = [1, 2, 3]
# all_sublists = [my_list[start_index:end_index] for start_index in range(len(my_list)) for end_index in range(start_index + 1, len(my_list) + 1)]
# print("All sublists:", all_sublists)
##############################
# my_list = [3, 1, 4, 1, 5, 9, 2]
# sorted_list = sorted(my_list)
# print("Original list:", my_list)
# print("Sorted list:", sorted_list)
# ##############################
# n = 5
# original_list = [1, 2, 3]
# new_list = original_list + list(range(1, n + 1))
# print("Original list:", original_list)
# print("New list:", new_list)
# ##############################
# import uuid
# unique_id = uuid.uuid4()
# print("Unique ID:", unique_id)
# ##############################
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_elements = list(set(list1) & set(list2))
# print("List 1:", list1)
# print("List 2:", list2)
# print("Common elements:", common_elements)
# ##############################
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 2
# my_list[::n], my_list[1::n] = my_list[1::n], my_list[::n]
# print("Original list:", my_list)
# ##############################
# integers = [1, 2, 3, 4, 5]
# combined_integer = int(''.join(map(str, integers)))
# print("Original integers:", integers)
# print("Combined integer:", combined_integer)
# ##############################
# my_list = ["apple", "banana", "orange", "kiwi", "grape"]
# result_dict = {}
# for word in my_list:
#     initial_char = word[0].lower()
#     if initial_char not in result_dict:
#         result_dict[initial_char] = []
#     result_dict[initial_char].append(word)
#
# print("Original list:", my_list)
# print("Split list:", result_dict)
# ##############################
# num_lists = 3
# lists = [[] for _ in range(num_lists)]
# print("Number of lists:", num_lists)
# print("Lists:", lists)
# ##############################
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# missing_values = list(set(list1) - set(list2))
# additional_values = list(set(list2) - set(list1))
# print("List 1:", list1)
# print("List 2:", list2)
# print("Missing values:", missing_values)
# print("Additional values:", additional_values)
# ##############################
# my_list = [1, 2, 3, 4, 5]
# var1, var2, var3, var4, var5 = my_list
# print("Original list:", my_list)
# print("Variables:", var1, var2, var3, var4, var5)
# ##############################
# start_number = 1
# group_of_numbers = list(range(start_number, start_number + 5))
# print("Group of five consecutive numbers:", group_of_numbers)
# ##############################
# start_number = 1
# group_of_numbers = list(range(start_number, start_number + 5))
# print("Group of five consecutive numbers:", group_of_numbers)
# ##############################
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_items = my_list[::2]
# print("Original list:", my_list)
# print("Odd items:", odd_items)
# ##############################
# my_list = [1, 2, 3, 4, 5]
# inserted_element = 0
# modified_list = [inserted_element, item for item in my_list]
# print("Original list:", my_list)
# print("Modified list:", modified_list)
# ##############################
# nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Nested lists:")
# for sublist in nested_lists:
#     print(sublist)
# ##############################
# list_of_dicts = [{}, {}, {}]  # Example list with dictionaries
# all_empty = all(not my_dict for my_dict in list_of_dicts)
# print("List of dictionaries:", list_of_dicts)
# print("Are all dictionaries empty?", all_empty)
# ##############################
# m, n = 3, 4  # Example values
# two_dimensional_array = [[i * j for j in range(n)] for i in range(m)]
# print("Two-dimensional array:")
# for row in two_dimensional_array:
#     print(row)
# ##############################
# my_list = ["apple", "banana", "orange"]
# capitalized_list = [word.upper() for word in my_list]
# print("Original list:", my_list)
# print("Capitalized list:", capitalized_list)
# ##############################
# my_list = ["apple", "banana", "orange"]
# reversed_and_uppercase = [word.upper() for word in reversed(my_list)]
# print("Original list:", my_list)
# print("Reversed and uppercase:", reversed_and_uppercase)
# ##############################
month_name = "February"
month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}
days = month_days.get(month_name, "Invalid month name")
print(f"{month_name} has {days} days.")
##############################


