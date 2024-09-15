import argparse
from encryption import encrypt_file, decrypt_file
from key_management import authenticate_user, generate_user_key, generate_user_secret, store_user_password

def main():
    parser = argparse.ArgumentParser(description='Encrypted File Storage CLI')
    subparsers = parser.add_subparsers(dest='command')

    encrypt_parser = subparsers.add_parser('encrypt')
    encrypt_parser.add_argument('file_path', help='Path to the file to encrypt')
    encrypt_parser.add_argument('-u', '--username', help='Username for authentication')

    decrypt_parser = subparsers.add_parser('decrypt')
    decrypt_parser.add_argument('file_path', help='Path to the encrypted file')
    decrypt_parser.add_argument('-u', '--username', help='Username for authentication')

    args = parser.parse_args()

    if args.command == 'encrypt':
        username = args.username
        password = input('Enter password: ')
        totp = input('Enter TOTP: ')
        if not authenticate_user(username, password, totp):
            print('Authentication failed')
            return

        file_path = args.file_path
        encrypted_data, file_hash = encrypt_file(file_path)

        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)

        print('File encrypted successfully')

    elif args.command == 'decrypt':
        username = args.username
        password = input('Enter password: ')
        totp = input('Enter TOTP: ')
        if not authenticate_user(username, password, totp):
            print('Authentication failed')
            return

        file_path = args.file_path
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = decrypt_file(encrypted_data, None)

        with open(file_path[:-4], 'wb') as f:
            f.write(decrypted_data)

        print('File decrypted successfully')

if __name__ == '__main__':
    main()
