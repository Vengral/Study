Task
Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

Notes :
Array/list size is at least 3 .

Array/list numbers could be a mixture of positives , negatives and zeros .

Repetition of numbers in the array/list could occur , So (duplications are not included when summing).


def max_tri_sum(numbers):
    new_l = []
    
    for i in range(3):
        maxi = max(numbers)
        while maxi in new_l:
            numbers.remove(maxi)
            maxi = max(numbers)
        new_l.append(maxi)
    
    print(new_l)
    return sum(new_l)
