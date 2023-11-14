Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3



def highest_rank(arr):
    
    my_dict = {}
    
    for i in arr:
        if i not in my_dict.keys():
            my_dict[i] =1
        else:
            my_dict[i] +=1
            
    max_count = max(my_dict.values())
    max_freq_numbers = [num for num, count in my_dict.items() if count == max_count]
    return max(max_freq_numbers)
    pass
