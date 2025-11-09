# check if a persion is eligible to vote or not using a functional prpramming approach
# using lambda function

age = int(input("Enter your age: "))
check_voting_eligibility = lambda age: "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(check_voting_eligibility(age))

# use map to find the greatest element in the given list
list1 = [10, 20, 30, 40, 50]
greatest_element = lambda x: max(x)
print("Greatest element in the list is:", greatest_element(list1))
# write a python program to filter out all the odd numbers using filter() and a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check_odd = lambda x: x % 2 != 0
print("Odd numbers in the list are:", list(filter(check_odd, numbers)))


# write a python program to first filter out the odd numbers and then square the remaining even numbers using filter(), map(), and lambda functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_odd = lambda x: x % 2 != 0
filter_even = lambda x: x % 2 == 0
square_filter_even = lambda x: x ** 2
print("Odd numbers after filtering are:", list(filter(filter_odd, numbers)))
print("Squared even numbers after filtering odd numbers are:", list(map(square_filter_even, filter(filter_even, numbers))))


# give a dictionary having names and ages. write a python program to filter out all the names of people who are above 18 years old using filter() and a lambda function
dict1 = {'Alice': 17, 'Bob': 20, 'Charlie': 18, 'David': 22, 'Eve': 15}
filter_above_18 = lambda x: x[1] > 18
print("Names of people above 18 years old are:", list(map(lambda x: x[0], filter(filter_above_18, dict1.items()))))


