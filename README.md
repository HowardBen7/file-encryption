File Encryption Tool
This Python script allows you to encrypt and decrypt files using a symmetric encryption algorithm.

Dependencies
This script uses the cryptography library. You can install this using pip:

Copy code
pip install cryptography
How to Use
Generate Encryption Key
Before you can encrypt or decrypt files, you need an encryption key. This script does not include functionality to generate keys. You can generate a key separately by using the following Python code:

python
Copy code
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
Store this key somewhere safe. If you lose the key, you won't be able to decrypt your data.

Encrypt a File
To encrypt a file, run the script and type e when asked if you want to encrypt or decrypt. Then, provide the name of the file you want to encrypt (make sure this file is in the same directory as the script or provide the full path) and enter the encryption key that you generated previously.

Example:

mathematica
Copy code
Do you want to (e)ncrypt or (d)ecrypt? e
Enter the file name: document.txt
Enter the encryption key: YOUR_ENCRYPTION_KEY_HERE
File encrypted.
Decrypt a File
To decrypt a file, run the script and type d when asked if you want to encrypt or decrypt. Then, provide the name of the file you want to decrypt (this file should be in the same directory as the script or provide the full path) and enter the encryption key that was used to encrypt the file.

Example:

mathematica
Copy code
Do you want to (e)ncrypt or (d)ecrypt? d
Enter the file name: document.txt
Enter the encryption key: YOUR_ENCRYPTION_KEY_HERE
File decrypted.
Note
Please remember that this script performs encryption in place. That means it replaces the original file with the encrypted/decrypted version. You might want to create copies of your files before encrypting or decrypting them as a precaution.

Conclusion
This is a simple file encryption tool created in Python. It's essential to keep the encryption key secure; without it, the encrypted data cannot be recovered. Use this script responsibly and remember to keep backups of your important data.