def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    num1 = a % 10 
    a = a//10
    num2 = a % 10

    if num2 > num1:
        natija = "True"
    if num2 < num1:
        natija = "False"
    return natija