Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    convert = [str(i) for i in arr]
    
    return int(max(convert, key=len))
