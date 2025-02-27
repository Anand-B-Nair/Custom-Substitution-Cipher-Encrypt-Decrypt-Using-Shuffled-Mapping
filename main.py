import random

original_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~")

random.seed(50)  # Fix the seed to keep the same shuffled order
shuffled_chars = original_chars.copy()  
random.shuffle(shuffled_chars)  

encrypt_dict = {original_chars[i]: shuffled_chars[i] for i in range(len(original_chars))}
decrypt_dict = {shuffled_chars[i]: original_chars[i] for i in range(len(original_chars))}

# Function to encrypt a message
def encrypt(text):
    return "".join(encrypt_dict.get(char, char) for char in text)  # Encrypt using the mapping

# Function to decrypt a message
def decrypt(text):
    return "".join(decrypt_dict.get(char, char) for char in text)  # Decrypt using the mapping

codeword = input("Enter the codeword: ")

# Encrypt and Decrypt
encrypted_text = encrypt(codeword)
print(f"Encrypted code: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Decrypted code: {decrypted_text}")
