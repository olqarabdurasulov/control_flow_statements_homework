def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0 and a%2 == 1:
        natija = "positive odd number"
    if a > 0 and a%2 == 0:
        natija = "positive even number"
    if a < 0 and a%2 == 1:
        natija = "negative odd number"
    if a < 0 and a%2 == 0:
        natija = "negative even number"
    if a == 0:
        natija = "the number is zero"
    return natija
