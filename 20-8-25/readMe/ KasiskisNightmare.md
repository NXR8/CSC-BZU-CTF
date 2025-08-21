# 🧬 Kasiski's Nightmare

## 🧩 Given Information:

- **Key Digest**: `e135a067fc096a19d7eb5ac64efd8bab3ff24010`
- **Ciphertext**: `LWT-VHU{O4Z2_Y9n_D1R7zcvk_WJPS73}`
- **Alphabet**: `abcdefghijklmnopqrstuvwxyz0123456789`  
- **Algorithm**: From the name of the question we conclude that the encryption algorithm is **Vigenère**

---

## 🔍 Step 1: Crack the Key Digest

#### Use [CrackStation](https://crackstation.net/) to crack key digest:

- **Input:** `e135a067fc096a19d7eb5ac64efd8bab3ff24010`
- **Output:** `Jerusalem`

## 🔐 Step 2: Vigenère Cipher Decryption

#### Use [DCode's Vigenère Cipher Tool](https://www.dcode.fr/vigenere-cipher) to decrypt the encrypted text using the key `Jerusalem`.

- **Decrypted Result:** `CSC-BZU{D0NT_US3_V1G3n3r3_C1PH3R}`

- ✅ **Final Flag:** `CSC-BZU{D0NT_US3_V1G3n3r3_C1PH3R}`
