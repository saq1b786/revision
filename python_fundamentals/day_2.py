# problem 1 sum numbers 

def sum_numbers(numbers: list):

    total = 0 

    for num in numbers: 
        total = total + num
    return total 
    
print(sum_numbers([1, 2, 3, 4, 5]))

# problem 2 

def count_even(numbers): 
    even_numbers = 0 

    for num in numbers: 
        if num % 2 == 0: 
            even_numbers += 1 
    return even_numbers

print(count_even([1, 2, 3, 4, 6]))

#problem 3 - bad version. because I have to do multiple searches

def find_index(numbers: list, target: int): 

    for num in numbers: 
        if num == target: 
            return numbers.index(num)

    return -1

# problem 3 good version. -  because using enum we alredy have the index at hand! so we dont need to do another search for the index

def find_index_2(numbers: list, target: int): 
    for index, num in enumerate(numbers): 
        if num == target: 
            return index
    return -1

print(find_index([10, 20, 30, 40], 30))
print(find_index_2([10, 20, 30, 40], 30))

# problem 4 

def reverse_string(text: str): 
    reverse_string = ''
    for i in text: 
        reverse_string = i + reverse_string
    return reverse_string

print(reverse_string('hello'))

#problem 5
def find_max(numbers):
    max_num = numbers[0]

    for num in numbers: 
        if num > max_num: 
            max_num = num 
    return max_num

print(find_max([3, 7, 2, 9, 4]))
print(find_max([-5, -2, -10]))

#problem 6
def count_occurrences(numbers: list, target: int): 
    count = 0 

    for num in numbers: 
        if num == target: 
            count += 1 
    return count

print(count_occurrences([1, 2, 2, 3, 2, 4], 2))

#problem 7 

def reverse_loop(text: str): 
    rev = ''

    for char in text: 
        rev = char + rev
    return rev

print(reverse_loop('cat'))