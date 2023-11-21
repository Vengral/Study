Task
Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

Notes
Array/list will contain positives only .
Array/list will always have even size
Input >> Output Examples
minSum({5,4,2,3}) ==> return (22) 
Explanation:
The minimum sum obtained from summing each two integers product ,  5*2 + 3*4 = 22
minSum({12,6,10,26,3,24}) ==> return (342)
Explanation:
The minimum sum obtained from summing each two integers product ,  26*3 + 24*6 + 12*10 = 342


def min_sum(arr):
    
    result = 0
    b = int(len(arr)/2)
    for i in range(b):
        maxi = max(arr)
        mini = min(arr)
        result += maxi*mini
        arr.remove(max(arr))
        arr.remove(min(arr))
        
    return result
    # Your code here
    pass

def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))
