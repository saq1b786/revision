#sum numbers
def sum_numbers(numbers:list):
    total = 0
    for num in numbers: 
        total+=num

    return total

print(sum_numbers([2, 4, 6, 8]))

#counter
def count_even(numbers:list): 

    count = 0
    for num in numbers: 
        if num % 2==0: 
            count = count + 1

    return count
print(count_even([1, 2, 4, 7, 9, 10]))

#searching
def find_index(numbers:list, target:int): 
    for index, num in enumerate(numbers): 
        if num == target: 
            return index

    return -1 

print(find_index([10, 20, 30, 40], 30))
print(
find_index([10, 20, 30, 40], 99))

#Reverse string 
def reverse_string(text:str): 
    reverse = ''
    for char in text: 
        reverse = char + reverse
    return reverse

print(reverse_string("hello"))

#find the maximum 
def find_max(numbers:list): 
    seen = numbers[0]
    for num in numbers: 
        if num > seen: 
            seen = num
    return seen

print(find_max([-8, -3, -12, -1]))

#Duplicate detecttion
def has_duplicate(numbers:list): 
    seen = set()
    for num in numbers: 
        if num in seen: 
            return True
        seen.add(num)
    return False
print(has_duplicate([1, 2, 3, 4]))
print(has_duplicate([1, 2, 3, 2]))

#frequency counting 
def count_numbers(numbers:list): 
    count = {}
    for num in numbers: 
        if num in count: 
            count[num] = count[num]+ 1 
        else: 
            count[num] = 1
    return count
print(count_numbers([1, 2, 2, 3, 2, 4, 4]))

#twoSum
def two_sum(numbers:list, target:int): 
    count = {}
    for index, num in enumerate(numbers): 
        needed = target - num 
        if needed in count: 
            return [count[needed], index]
        
        count[num] = index
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))

    