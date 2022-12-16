def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 9 and a < 99 and a%2 == 1:
        natija = "two-digit odd number"
    if a > 9 and a < 99 and a%2 == 0:
        natija = "two-digit even number"
    if a > 99 and a < 999 and a%2 == 1:
        natija = "three-digit odd number"
    if a > 99 and a < 999 and a%2 == 0:
        natija = "three-digit even number"
    
    return natija