import string

def caesar_encrypt(message, key):
    """
    Encrypts a message using the Caesar cipher with a given key.

    Args:
        message (str): The message to encrypt.
        key (int): The shift value for the Caesar cipher (0-25).

    Returns:
        str: The encrypted message.
    """

    # Calculate the Caesar shift value by taking the modulo of the key with 26
    # This ensures the shift stays within the range of the alphabet (0-25)
    shift = key % 26

    # Create a translation table for encryption
    # We use str.maketrans to create a mapping between characters
    # The first argument specifies the source characters (lowercase alphabet)
    # The second argument defines the new order for the encrypted characters
    # We achieve this by slicing the alphabet with the shift value
    #  - string.ascii_lowercase[shift:] represents the characters after the shift
    #  - string.ascii_lowercase[:shift] represents the characters before the shift
    # These characters are concatenated to create the new order
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    # Convert the message to lowercase for case-insensitive encryption
    message = message.lower()

    # Apply the translation table to the message
    # This translates each character in the message according to the cipher
    encrypted_message = message.translate(cipher)

    return encrypted_message


def caesar_decrypt(encrypted_message, key):
    """
    Decrypts a message encrypted with the Caesar cipher using a given key.

    Args:
        encrypted_message (str): The encrypted message to decrypt.
        key (int): The shift value used for encryption (0-25).

    Returns:
        str: The decrypted message.
    """

    # Calculate the decryption shift value
    # Since decryption involves shifting back by the key positions,
    # we calculate 26 minus the modulo of the key with 26
    shift = 26 - (key % 26)

    # Create a translation table for decryption
    # Similar to encryption, we create a table to shift characters back
    #  - string.ascii_lowercase[shift:] represents the characters that were shifted after the original encryption
    #  - string.ascii_lowercase[:shift] represents the characters that were shifted before the original encryption
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    # Apply the translation table to the encrypted message
    message = encrypted_message.translate(cipher)

    return message

# Example usage
message = 'Subscribe To W J Pearce'
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
