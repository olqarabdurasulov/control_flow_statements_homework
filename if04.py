def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    positive_numbers = 0
    if a > 0:
        positive_numbers += 1
    if b > 0:
        positive_numbers += 1
    if c > 0:
        positive_numbers += 1
    return positive_numbers