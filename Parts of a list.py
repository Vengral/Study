Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.

Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C: see Examples test Cases - )
Each part will be in a string
Elements of a pair must be in the same order as in the original array.

  def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        part1 = ' '.join(arr[:i])
        part2 = ' '.join(arr[i:])
        result.append((part1, part2))
    return result
    # your code
