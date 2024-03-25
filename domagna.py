def intToDecimal(num, decimals):
    """
    Converts an integer to a decimal string with the specified number of decimal places.

    Args:
        num: The integer to convert.
        decimals: The number of decimal places to include in the string.

    Returns:
        A string representing the decimal value of the integer.
    """

    if decimals < 0:
        raise ValueError("Decimals must be non-negative")

    # Convert the integer to a string
    num_str = str(num)

    # If the number of decimals is 0, return the integer string
    if decimals == 0:
        return num_str

    # Otherwise, insert a decimal point and add the specified number of zeros
    else:
        return num_str + "." + "0" * (decimals - len(num_str.split(".")[1]))
