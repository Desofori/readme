import os
import hashlib
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY_FILE = 'key.bin'

def generate_key():
    key = os.urandom(32)
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    else:
        return generate_key()

def encrypt_file(file_path):
    key = load_key()
    
    # Open the file and read its contents
    with open(file_path, 'rb') as file:
        file_data = file.read()

    file_hash = hashlib.sha256(file_data).hexdigest()

    # Generate a random IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data, file_hash  # Prepend IV to the encrypted data

def decrypt_file(encrypted_data, file_hash):
    key = load_key()
    
    # Extract IV from the encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    decrypted_file_hash = hashlib.sha256(decrypted_data).hexdigest()

    if decrypted_file_hash != file_hash:
        raise ValueError("File integrity check failed")

    return decrypted_data
