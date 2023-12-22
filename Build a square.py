I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer will be a whole number between 1 and 50.

Example
n = 3, so I expect a 3x3 square back just like below as a string:

+++
+++
+++


def generate_shape(n):
    
    square = ""
    for i in range(n):
        for j in range(n):
            square+="+"
        square+="\n"
    return square[:-1]
    pass
