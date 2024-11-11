def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character by the key value, wrapping around to 'A'/'a' if necessary
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back by the key value, wrapping around to 'A'/'a' if necessary
            if char.isupper():
                plaintext += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    return plaintext


def main():

    # Prompt the user to enter the plaintext or ciphertext
    text = input("Enter the text: ")


    # Prompt the user to enter the key
    while True:
        key = input("Enter the key (1-26): ")
        if key.isdigit() and 1 <= int(key) <= 26:
            key = int(key)
            break
        else:
            print("Invalid key. Please enter a number between 1 and 26.")

    # Prompt the user to choose encryption or decryption
    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\nEnter your choice: ")
        if choice == "1":
            print("Ciphertext:", encrypt(text, key))
            break
        elif choice == "2":
            print("Plaintext:", decrypt(text, key))
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()