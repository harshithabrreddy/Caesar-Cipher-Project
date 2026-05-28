# Caesar Cipher Project

# Function to Encrypt
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        # Check uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

        # Keep spaces/symbols same
        else:
            encrypted_text += char

    return encrypted_text


# Function to Decrypt
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:

        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += char

    return decrypted_text


# Main Program
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")

shift = int(input("Enter key/shift value: "))

encrypted = encrypt(message, shift)

print("\nEncrypted Message:", encrypted)

decrypted = decrypt(encrypted, shift)

print("Decrypted Message:", decrypted)