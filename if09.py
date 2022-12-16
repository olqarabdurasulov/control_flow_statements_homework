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
    num0 = a
    num1 = num0 % 10 
    num0 = num0//10
    num2 = num1*10 + num0

    return num2 > a
    # if num2 < a:
    #     return True
    # if num2 > a:
    #     return False
