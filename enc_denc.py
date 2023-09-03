
from cryptography.fernet import Fernet

# Generate a secret key for encryption (keep this key secret and secure)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Simulate a sensitive data entry (e.g., credit card number)
sensitive_data = "1234-5678-9012-3456"

# Encrypt the sensitive data
encrypted_data = cipher_suite.encrypt(sensitive_data.encode())

# Decrypt the sensitive data
decrypted_data = cipher_suite.decrypt(encrypted_data).decode()

print("Original Data:", sensitive_data)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)

