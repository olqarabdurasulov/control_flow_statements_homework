def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    natija = 0
    if a == 0:
        natija = 10

    if a > 0:
        natija += 1

    if a < 1:
        natija -= 2
    
    return natija