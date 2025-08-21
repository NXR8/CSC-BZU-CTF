# 🔓 Hash Cracker

## 🧩 Given Information:

- **[Archive file](../content/ab4854338885a0c2b055ea2344b84e0e601ce995f4e548db4422d7b29a293dac.zip)**
- **[Code for encryption](../content/EncDES.py)**

## 🔍 Step 1: Open archive file

#### Use [CrackStation](https://crackstation.net/) to crack archive file name:

- **Input:** `ab4854338885a0c2b055ea2344b84e0e601ce995f4e548db4422d7b29a293dac`
- **Output:** `GazaGaza`

After open archive file we get ***Enc*** file, Enc content is: `3a578c48f8fcd473f229c935d263ef4c1c372e2ccbd8dc9e5b4c91b04c3bac3ddf03e7a7935cebea0206f632bd4c4a18f54bb37e492228c748d86ecaf9f9ff49`


## 🤔 Step 2: Write decrypt method

```python
def decrypt_des(ciphertext_hex, key):
    """
    Decrypt text using DES (ECB mode)
    Inputs:
        ciphertext_hex (str): Encrypted text in hex format
        key (str): Decryption key (8 chars/bytes)
    Outputs:
        str: Decrypted original text
    """
    # Convert key to bytes
    key_bytes = key.encode('utf-8')
    
    # Convert hex ciphertext to bytes
    ciphertext_bytes = binascii.unhexlify(ciphertext_hex)
    
    # Create DES object with key
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    # Decrypt and remove padding
    decrypted_bytes = unpad(cipher.decrypt(ciphertext_bytes), DES.block_size)
    
    # Convert result back to string
    decrypted_text = decrypted_bytes.decode('utf-8')
    return decrypted_text
```

## 🔐 Step 3: Run decryption method

```python
key = "GazaGaza"
ct = "3a578c48f8fcd473f229c935d263ef4c1c372e2ccbd8dc9e5b4c91b04c3bac3ddf03e7a7935cebea0206f632bd4c4a18f54bb37e492228c748d86ecaf9f9ff49"
flag = decrypt_des(ct, key)
```

- ✅ **Final Flag:** `CSC-BZU{1_UsEd_DES_th1s_t1mE...NExt_1'll_usE_TripleDES!}`
