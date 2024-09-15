• 👋 Hi, I’m Desmond Ofori Asare

• 👀 I’m interested in cybersecurity, Networking, programming and web development

• 🌱 I’m currently learning Javascript & React with 60% knowledge in JS.

• 🧑🏽‍💻 I'm good in HTML/CSS, Python, Wireshark, Nmap and CMD

• 💞️ I’m looking to collaborate on with cyber personnels and Programmers since that is my field

• 📫 How to reach me on my mail desmondsutt84@gmail.com

• 😄 Pronouns: Cyber Security || Computer Science|| Programming || Problem Solving || Data Structures 

• ⚡ Fun fact: I love to sleep a lot(PRIORITY) therefore finish my projects on time.

---

# File Encryption & Decryption with User Authentication (TOTP)

## Overview

This project demonstrates a secure file encryption and decryption system using Python. It incorporates user authentication via password and TOTP (Time-based One-Time Password), and securely manages user-specific keys for encrypting and decrypting files. 

### Key Features:
- **256-bit AES Encryption**: Secure encryption using Advanced Encryption Standard (AES) in CBC mode.
- **User Authentication**: Users authenticate with both a password and a TOTP generated via the `pyotp` library.
- **Key Management**: Each user is assigned a unique key for encryption, securely stored in a file.
- **Password Hashing**: Passwords are securely stored using `bcrypt` hashing.
- **CLI Interface**: A command-line interface allows users to encrypt and decrypt files.
- **Comprehensive Testing**: Unit and integration tests using `unittest` and `pytest`.

---

## Project Structure

- **encryption.py**: Handles file encryption and decryption using AES.
- **key_management.py**: Manages user keys, secrets, and authentication.
- **cli.py**: A command-line interface to encrypt and decrypt files.
- **test_cli.py**: Integration tests for the CLI.
- **test_key_management.py**: Unit tests for key management and authentication.

---

## Requirements

- Python 3.6+
- Libraries:
  - `cryptography`
  - `pyotp`
  - `bcrypt`
  - `pytest` (for testing)
  - `unittest`

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Desofori/readme
    cd readme
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) If you haven't created a `requirements.txt`, use:
    ```bash
    pip install cryptography pyotp bcrypt pytest
    ```

---

## How to Use

The system can be used via the command-line interface (CLI) to encrypt and decrypt files after successful user authentication.

### 1. Encryption

Encrypt a file using the following command:

```bash
python cli.py encrypt path/to/your/file -u username
```

You will be prompted for:
- **Password**: The user’s password.
- **TOTP**: The one-time password from your TOTP generator (e.g., Google Authenticator).

If authentication succeeds, the file will be encrypted, and an `.enc` file will be generated.

### 2. Decryption

To decrypt a previously encrypted file:

```bash
python cli.py decrypt path/to/your/encrypted/file.enc -u username
```

Again, you will be prompted for the password and TOTP. If authentication is successful, the file will be decrypted and saved without the `.enc` extension.

---

## User Setup

To register a new user:
1. Generate the user’s encryption key and store the password:

```python
from key_management import store_user_password, generate_user_secret

store_user_password("username", "your_password")
generate_user_secret("username")
```

2. Store the secret in your TOTP app (e.g., Google Authenticator) for generating codes.

---

## Running Tests

This project uses both `unittest` and `pytest` for testing.

1. **Running Unit Tests with `unittest`**:

   To run tests for key management:
   ```bash
   python -m unittest test_key_management.py
   ```

2. **Running Integration Tests with `pytest`**:

   To run CLI tests:
   ```bash
   pytest test_cli.py
   ```

Tests ensure that the encryption, decryption, and user authentication functions behave correctly.

---

## Security Considerations

- **Password Security**: User passwords are hashed using `bcrypt` before being stored.
- **Key Storage**: Each user has a unique 256-bit encryption key stored securely.
- **Two-Factor Authentication**: TOTP (Time-based One-Time Password) is implemented for added security during authentication.
- **File Integrity**: The system checks file integrity by comparing the SHA-256 hash of the original and decrypted files.

---

## Future Improvements

Some potential improvements for the future:
- **Database Integration**: Currently, user keys and secrets are stored in memory. In a real-world application, these should be stored securely in a database or a key vault.
- **Password Reset Mechanism**: Implement a way for users to reset their passwords securely.
- **Improved User Interface**: Build a graphical user interface (GUI) for ease of use.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

[Desmond Ofori Asare] - [desmondscutt84@gmail.com]

---

<!---
Desofori/Desofori is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
