import os
import pytest
from cli import main

def test_encrypt_decrypt_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("Hello, World!")

    # Simulate CLI args
    args = ["encrypt", str(file_path), "-u", "test_user"]
    main(args)

    encrypted_file_path = str(file_path) + ".enc"
    assert os.path.exists(encrypted_file_path)

    args = ["decrypt", encrypted_file_path, "-u", "test_user"]
    main(args)

    assert os.path.exists(file_path)
    with open(file_path, 'r') as file:
        assert file.read() == "Hello, World!"
