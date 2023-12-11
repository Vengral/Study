Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return the string "None".

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'


def dashatize(n):
    if type(n) != int:
        return "None"
    n_str = str(abs(n))
    result = ""
    
    for i in n_str:
        if int(i) % 2 == 1:
            result += "-" + i + "-"
        else:
            result += i

            
    
    result = result.replace('--', '-')
    result = result.strip('-')
    return result
