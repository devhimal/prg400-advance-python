list = ["job", "james", "john", "jake"]
print(list)

# remove the 3rd element from the list
list.pop(2)
print("list after removing 3rd element:")
print(list)

# function that return sum of all elements in the list
num_list = [1, 2, 3, 4, 5]
def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print(sum_of_list(num_list))

# given two lists, write a program to create a new list that contains only the common elements between the two.
def common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2 and element not in common_list:
            common_list.append(element)
    return common_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print("Common elements between list1 and list2:")
print(result)

# Reverse a list without using a built-in function or method.
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

num_list = [1, 2, 3, 4, 5]
print("Original list:")
print(num_list)
reversed_num_list = reverse_list(num_list)
print("Reversed list:")
print(reversed_num_list)


# Give a tuple of numbers, write a program to find the maximum and minimum values.
person_tuple = (34, 12, 45, 67, 23, 89, 5)

def find_max_min(tpl):
    max_value = tpl[0]
    min_value = tpl[0]
    for num in tpl:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num
    return max_value, min_value
print("Tuple of numbers:")
print(person_tuple)
find_max, find_min = find_max_min(person_tuple)
print("Maximum value:", find_max)
print("Minimum value:", find_min)

# create a dictionary to store information about a book(title, author, year, publisher)
book_info = {
    "book1":{
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "publisher": "J.B. Lippincott & Co."
    },{
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "publisher": "Secker & Warburg"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "publisher": "Charles Scribner's Sons"
    },
}
