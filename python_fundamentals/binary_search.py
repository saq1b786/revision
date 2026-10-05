def binary_search(numbers:list, target: int): 
    left = 0 
    right = len(numbers) - 1 

    while left <= right: 
        middle = (left + right) // 2 

        if numbers[middle] == target: 
            return True
        elif numbers[middle] < target: 
            left = middle + 1  
        else: 
            right = middle - 1

    return False


print(binary_search([2, 4, 6, 8, 10, 12, 14, 16, 18], 16))
print(binary_search([2, 4, 6, 8, 10, 12, 14, 16, 18], 5))
print(binary_search([1, 3, 5, 7, 9], 1))
print(binary_search([1, 3, 5, 7, 9], 9))
        

def search(numbers: list, target: int): 
    left = 0 
    right = len(numbers) - 1 

    while left <= right: 
        middle = (left + right) // 2 

        if numbers[middle] == target: 
            return middle
        elif numbers[middle] < target: 
            left = middle + 1 
        else: 
            right = middle - 1 
    return -1 

def first_position(numbers: list, target: int): 
    left = 0 
    right = len(numbers) - 1 
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

