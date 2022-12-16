def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    negative_numbers = 0
    if a < 0:
        negative_numbers +=1
    if b < 0:
        negative_numbers +=1
    if c < 0:
        negative_numbers +=1
    return negative_numbers