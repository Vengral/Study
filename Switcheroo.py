Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'


def switcheroo(s):
    
    new_string = ""
    for i in s:
        if i == "c":
            new_string +="c"
        elif i =="a":
            new_string += "b"
        else:
            new_string += "a"
            
    return new_string


