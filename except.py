def get_operator_value(source):
    """
    This function can either return a new operator value or (if the source
    meets certain conditions) perform another action such as raising an error
    or returning a default value.

    Parameters:
    source (dict): A dictionary containing details about the operator.

    Returns:
    str: The new operator value.
    """

    # Check if 'operator' key exists in the source dictionary
    if 'operator' not in source:
        raise ValueError("Source does not contain an 'operator' key")
    
    # Retrieve the operator value from the source
    operator = source['operator']

    # Perform some conditional logic based on the operator value
    if operator == 'add':
        return '+'
    elif operator == 'subtract':
        return '-'
    elif operator == 'multiply':
        return '*'
    elif operator == 'divide':
        return '/'
    else:
        # If the operator is not recognized, return a default value
        return 'unknown'

# Example usage
source = {'operator': 'add'}
print(get_operator_value(source))  # Output: '+'

source = {'operator': 'unknown_op'}
print(get_operator_value(source))  # Output: 'unknown'
