import string

def AffineCipherEncrypt(message, key_x, key_y):
    letters = string.ascii_lowercase  # Uses Python’s built-in lowercase letters
    EncryptedMsg = ""

    for char in message:
        if char in letters:
            char_index = letters.index(char)  # Get index of character
            encrypted_index = (char_index * key_x + key_y) % len(letters)
            EncryptedMsg += letters[encrypted_index]
        else:
            EncryptedMsg += char  # Keep non-alphabet characters unchanged
    
    return EncryptedMsg


def main():
    message = input("Enter the message to encrypt: ").lower()  # Convert to lowercase for consistency

    try:
        key_x = int(input("Enter the key X: "))
        key_y = int(input("Enter the key Y: "))
    except ValueError:
        print("Invalid input! Keys must be integers.")
        return
    
    EncryptedMsg = AffineCipherEncrypt(message, key_x, key_y)
    print("Encrypted message:", EncryptedMsg)


if __name__ == "__main__":
    main()
