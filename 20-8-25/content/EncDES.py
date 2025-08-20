from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_des(plaintext, key):
    """
    Encrypt text using DES (ECB mode)
    Inputs:
        plaintext (str): Original text (must be multiple of 8 bytes after padding)
        key (str): Encryption key (8 chars/bytes)
    Outputs:
        str: Encrypted text in hex format
    """
    # Convert text and key to bytes
    key_bytes = key.encode('utf-8')
    plaintext_bytes = plaintext.encode('utf-8')
    
    # Create DES object with key
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    # Encrypt text with PKCS7 padding
    ciphertext_bytes = cipher.encrypt(pad(plaintext_bytes, DES.block_size))
    
    # Convert result to hex
    ciphertext_hex = binascii.hexlify(ciphertext_bytes).decode('utf-8')
    return ciphertext_hex


# ===== Usage Example =====

# Encryption example
key = "ItIskey."  # Must be exactly 8 characters
plaintext = "Help Gaza"
encrypted = encrypt_des(plaintext, key)
print(f"Encrypted text (hex): {encrypted}")
    
