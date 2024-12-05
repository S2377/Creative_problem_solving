def get_letters_for_digit(digit):
    """
    Returns the corresponding letters for a given digit on a phone keypad
    """
    digit_to_letters = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    return digit_to_letters.get(digit, [])

def get_combos_starting_from(phone_number, index):
    """
    Recursively generates all possible letter combinations starting from given index
    
    Args:
        phone_number (str): The input phone number
        index (int): Current position in the phone number
        
    Returns:
        List[str]: List of all possible letter combinations
    """
    # Base case: if we've processed all digits, return empty list
    if index == len(phone_number):
        return [""]
    
    # Get all combinations for the rest of the string
    combos = get_combos_starting_from(phone_number, index + 1)
    # print(type(combos))
    
    # Get letters corresponding to current digit
    current_digit = phone_number[index]
    # print(current_digit)
    letters_to_add = get_letters_for_digit(current_digit)
    
    # Generate new combinations by adding each letter to existing combinations
    result = []
    for combo in combos:
        for letter in letters_to_add:
            result.append(letter + combo)
            
    return result

def generate_mnemonics(phone_number):
    """
    Generates all possible letter combinations for a given phone number
    
    Args:
        phone_number (str): The input phone number
        
    Returns:
        List[str]: List of all possible letter combinations
    """
    # Filter out 0s and 1s from the phone number
    filtered_number = ''.join(digit for digit in phone_number if digit not in '01')
    
    # Generate all combinations
    return get_combos_starting_from(filtered_number, 0)

# Test the functionality
def test_mnemonics():
    test_cases = [
        "213",
        "456",
        "23"
    ]
    
    for number in test_cases:
        print(f"\nPhone number: {number}")
        mnemonics = generate_mnemonics(number)
        print(f"Possible combinations ({len(mnemonics)}):")
        print(', '.join(mnemonics))

if __name__ == "__main__":
    test_mnemonics()