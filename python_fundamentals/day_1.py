# problem 1
def find_max(numbers: list): 
    num = numbers[0]
    for i in numbers: 
        if i > num: 
            num = i 

    return num 

print(find_max([3, 7, 2, 9, 4]))

# problem 2 
def count_vowel(text: str): 
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0 

    for letter in text: 
        if letter in vowels: 
            count += 1
    return count


print(count_vowel('hello world'))

# problem 3 
def contains_duplicate(numbers: list): 
    seen = {}

    for item in numbers: 
        if item in seen: 
            return True
        seen.add(item)
    return False

    

print(contains_duplicate([1,2,3,4]))

# problem 4 
def reverse_string(text: str): 
    reverse_text = text[::-1]

    print(reverse_text)

reverse_string('hi')

# problem 5 two sum 

