def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
   
    if a == 0:
        natija = -2

    if a > 0:
        natija = a + 1

    if a < 1:
        natija = a - 2
    
    return natija
print(main(-2))