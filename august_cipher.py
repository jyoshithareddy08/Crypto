# Encryption Function
def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + 1) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + 1) % 26 + 65)
        else:
            result += char
    return result


# Decryption Function
def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 - 1) % 26 + 97)
            else:
                result += chr((ord(char) - 65 - 1) % 26 + 65)
        else:
            result += char
    return result


# Custom Hash Function
def simple_hash(text):
    hash_value = 0
    for char in text:
        hash_value = (hash_value * 31 + ord(char)) % 100000
    return hash_value

# Main Program
text = input("Enter text: ")
encrypted = encrypt(text)
decrypted = decrypt(encrypted)
hash_val = simple_hash(text)
print("\nEncrypted Text :", encrypted)
print("Decrypted Text :", decrypted)
print("Hash Value     :", hash_val)