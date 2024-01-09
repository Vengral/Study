Return an array/list where Even numbers come first then odds

Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .

Array/list size is at least 4 .

Array/list numbers could be a mixture of positives , negatives .

Have no fear , It is guaranteed that no Zeroes will exists .!alt
Repetition of numbers in the array/list could occur , So (duplications are not included when separating).


def men_from_boys(arr):
    
    arr = list(set(arr))
    even = [i for i in arr if i%2==0]
    odd = [i for i in arr if i%2==1]
    even.sort()
    odd.sort(reverse=True)
    
    return even+odd

