# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function. The first line of the code has been defined as below.

def hello_name(user_name):
    """Prints "hello_USERNAME!" where USERNAME is input by the user."""
    print('"Hello_' + user_name.upper() + '!"')

hello_name('bo')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    """Prints the odd numbers from 1-100 and returns nothing."""
    for n in range(1,100):
        if n % 2 == 1:
            print(n)
    return
    
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a 
# given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Returns the max number of a given list."""
    max_num = 0
    for a in a_list:
        if a > max_num:
            max_num = a
        else:
            continue
    return(max_num)

max_num_in_list([7, 2, 4, 9, 17, 1, 3, 6, 5])

                
# Question 4
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Returns if the given year is a leap year."""
    if a_year % 400 == 0:
        return(True)
    elif a_year % 100 == 0:
        return(False)
    elif a_year % 4 == 0:
        return(True)
    else:
        return(False)

print(is_leap_year(2022)) # Not a Leap Year
print(is_leap_year(2000)) # Leap Year
print(is_leap_year(1900)) # Not a Leap Year
print(is_leap_year(2016)) # Leap Year

                
# Question 5
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
# are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Returns a boolean if all numbers in list are consecutive numbers."""
    new_list = []
    for a in a_list:
        if len(new_list) == 0:
            new_list.append(a)
            continue
        elif a == new_list[:].pop() + 1:
            new_list.append(a)
        elif a == new_list[:].pop() - 1:
            new_list.append(a)
        else:
            return(False)
    return(True)

print(is_consecutive([4, 5, 6, 7, 8, 9])) # consecutive
print(is_consecutive([4, 5, 6, 2, 8, 9])) # not consecutive
print(is_consecutive([8, 7, 6, 5, 4, 3])) # consecutive
print(is_consecutive([8, 7, 9, 5, 4, 3])) # not consecutive
print(is_consecutive([-16, -15, -14, -13, -12, -11, -10])) # consecutive
print(is_consecutive([-16, -15, -14, 13, -12, -11, -10])) # not consecutive
print(is_consecutive([-7, -8, -9, -10, -11, -12, -13, -14, -15])) # consecutive
print(is_consecutive([-7, -8, -9, 10, -11, -12, -13, -14, -15])) # not consecutive