from cryptography.fernet import Fernet
import sys

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_name, key):
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_name, key):
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    action = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    file_name = input("Enter the file name: ")
    key = input("Enter the encryption key: ").encode()

    if action == 'e':
        encrypt_file(file_name, key)
        print("File encrypted.")
    elif action == 'd':
        decrypt_file(file_name, key)
        print("File decrypted.")
    else:
        print("Invalid option")