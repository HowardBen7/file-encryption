# Import the necessary modules from the cryptography library
from cryptography.fernet import Fernet
import sys

# Function to generate a random encryption key
def generate_key():
    # Return a newly generated key
    return Fernet.generate_key()

# Function to encrypt a file
def encrypt_file(file_name, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)

    # Open the file to be encrypted in binary read mode
    with open(file_name, "rb") as file:
        # Read the contents of the file
        file_data = file.read()

    # Encrypt the contents of the file
    encrypted_data = fernet.encrypt(file_data)

    # Open the file in binary write mode
    with open(file_name, "wb") as file:
        # Write the encrypted data back to the file
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_name, key):
    # Create a Fernet object with the provided key
    fernet = Fernet(key)

    # Open the file to be decrypted in binary read mode
    with open(file_name, "rb") as file:
        # Read the encrypted contents of the file
        encrypted_data = file.read()

    # Decrypt the contents of the file
    decrypted_data = fernet.decrypt(encrypted_data)

    # Open the file in binary write mode
    with open(file_name, "wb") as file:
        # Write the decrypted data back to the file
        file.write(decrypted_data)

# Main execution starts here
if __name__ == "__main__":
    # Ask the user for the action (encrypt or decrypt)
    action = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    # Ask the user for the file name
    file_name = input("Enter the file name: ")
    # Ask the user for the encryption key
    key = input("Enter the encryption key: ").encode()

    # If the user chooses to encrypt
    if action == 'e':
        # Call the encrypt_file function
        encrypt_file(file_name, key)
        # Inform the user that the file has been encrypted
        print("File encrypted.")
    # If the user chooses to decrypt
    elif action == 'd':
        # Call the decrypt_file function
        decrypt_file(file_name, key)
        # Inform the user that the file has been decrypted
        print("File decrypted.")
    # If the user enters an invalid option
    else:
        # Inform the user that the option is invalid
        print("Invalid option")