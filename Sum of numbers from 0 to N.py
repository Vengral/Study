We want to generate a function that computes the series starting from 0 and ending until the given number.

  def show_sequence(n):
    if n ==0:
        return "0=0"
    elif n<0:
        return str(n)+"<0"
    else:
        sum=0
        result=""
        for i in range(0,n+1):
            sum +=i
            result += str(i)+"+"
    result = result[:len(result)-1]
    return result + " = " + str(sum)
    pass
