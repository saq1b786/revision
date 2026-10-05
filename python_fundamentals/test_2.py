#sum of all even numbers
def sum_even(numbers: list): 
    sum = 0 

    for num in numbers: 
        if num % 2 == 0: 
            sum = sum + num
    return sum
print(sum_even([1, 2, 3, 4, 6]))

#list contains duplicates

def has_duplicates(numbers:list): 
    seen = set()
    for num in numbers: 
        if num in seen: 
            return True 

        seen.add(num)
    return False

print(has_duplicates([1,2,3,4,5]))

#number frequency

def count_numbers(numbers:list): 
    count = {}

    for num in numbers:
        if num in count:
            count[num] = count[num] + 1 
        else: 
            count[num] = 1 
    return count

print(count_numbers([1, 2, 2, 3, 3, 3]))

#two sum 

def two_sum(numbers:list, target:int): 
    seen = {}
    for index, num in enumerate(numbers): 
        needed = target - num 
        if needed in seen: 
            return [seen[needed], index]
        seen[num] = index
    
print(two_sum([2, 7, 11, 15], 9))

        
# Q5: Time = O(n) , Space: O(1)

#Binary Search

def search(numbers:list, target:int): 
    left = 0
    right = len(numbers) - 1 

    while left<= right: 
        middle = (left+ right) //2 

        if numbers[middle] == target: 
            return middle
        elif numbers[middle] < target: 
            left +=1
        else: 
            right -= 1 
    return -1

print(search([1, 3, 5, 7, 9], 7))
print(search([1, 3, 5, 7, 9], 4))

#first occurence
def first_position(numbers: list, target: int): 
    left = 0 
    right = len(numbers) -1 
    answer = -1 
    while left <= right: 
        middle = (left + right) //2 
        if numbers[middle] == target: 
            answer = middle
            right = middle - 1

        elif numbers[middle] < target: 
            left = middle + 1 
        else: 
            right = middle -1 
    return answer
print(first_position([1, 2, 4, 4, 4, 6, 8], 4))



#two pointers

def two_sum_sorted(numbers: list, target:int): 
    left = 0
    right = len(numbers) -1 
    while left <= right: 
        answer = numbers[left] + numbers[right] 
        if answer == target: 
            return True 
        elif answer < target: 
            left += 1 
        else: 
            right -= 1
    return False

print(two_sum_sorted([1, 2, 4, 6, 8, 9], 10))
print(two_sum_sorted([1, 2, 4, 6, 8, 9], 20))