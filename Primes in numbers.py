Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 (p1**n1)(p2**n2)...(pk**nk)
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return (2**5)(5)(7**2)(11)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    result = ""
    divisor = 2 

    while n > 1:
        count = 0  
        while n % divisor == 0 and is_prime(divisor):
            n //= divisor
            count += 1

        if count > 0:
            result += f"({divisor}"
            if count > 1:
                result += f"**{count}"
            result += ")"

        divisor += 1

    return result
