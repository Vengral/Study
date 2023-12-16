A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Task
Given a number determine if it Automorphic or not .

def automorphic(n):
    
    b = n**2
    
    if str(b).endswith(str(n)):
        return "Automorphic"
    else:
        return "Not!!"
    #your code here
