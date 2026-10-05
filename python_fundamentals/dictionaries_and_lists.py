# sets are used for 'have i seen this before' problems. they are unordered and unique.
# or for duplicates problems. when a questions asks that use a set. They store unique values and are unordered.

# problem 1

def has_duplicate(numbers: list): 
    seen = set()
    for num in numbers: 
        if num in seen:
            return True
            
        else: 
            seen.add(num)
        
    return False

print(has_duplicate([1, 2, 3, 4]))
print(has_duplicate([1, 2, 3, 2]))
print(has_duplicate([5, 5]))

# dictionaries - remember info about things I have seen. 

def count_numbers(numbers:list): 
    count = {}

    for num in numbers: 
        if num in count: 
            count[num] = count[num] + 1
        else: 
            count[num] = 1

    return count

print(count_numbers([1, 2, 2, 3, 2, 4, 4]))
    