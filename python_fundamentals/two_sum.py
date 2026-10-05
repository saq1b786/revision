# two sum problems 

def two_sums(numbers: list, target: int): 
    seen = {}

    for index, num in enumerate(numbers): 

        needed = target - num

        if needed in seen: 
            return [seen[needed], index]

        seen[num] = index

print(two_sums([2, 7, 11, 15], 9))
print(two_sums([3, 2, 4], 6))


def two_sumss(numbers: list, target: int): 
    seen = {}

    for i, num in enumerate(numbers): 
        needed = target - num
        if needed in seen: 
            return [seen[needed], i]
        seen[num] = i

print(two_sumss([2, 7, 11, 15], 9))
print(two_sumss([3, 2, 4], 6))

print(two_sumss([2, 7, 11, 15], 9))
print(two_sumss([3, 2, 4], 6))
print(two_sumss([6, 4, 13, 9, 2], 11))