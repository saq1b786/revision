#two pointers first attempt 
def two_sum_sorted(numbers: list, target: int): 

    left = 0 
    right = len(numbers) - 1 


    while left <= right: 
        answer = numbers[left] + numbers[right]
        if answer == target: 
            return True
        elif answer < target: 
            left += 1
        else: 
            right -= 1 

    return False
    

