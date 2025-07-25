# 🔓 Hash Cracker

## 🧩 Given Information:

- **Key Digest (MD5):** `008ced81ddf77a45e35513f4459d7baf`
- **Encrypted Data:** `KCTCSZFTHVQMAEEWOIBO`
- **Flag Format:** `CSC-BZU{THIS_IS_FLAG_FORMATE}`

## 🔍 Step 1: Crack the Key Digest

Use [CrackStation](https://crackstation.net/) to crack the MD5 hash:

- **Input:** `008ced81ddf77a45e35513f4459d7baf`
- **Output:** `Palestine`

## 🔐 Step 2: PlayFair Cipher Decryption

Use [DCode's PlayFair Cipher Tool](https://www.dcode.fr/playfair-cipher) to decrypt the encrypted text using the key `Palestine`.

![Insert Screenshot or Tool Output Here](../image/HashCracker.png)

- **Decrypted Result:** `CSCBZUDIDYOUPLAYFAIR`

Apply the flag format:

- ✅ **Final Flag:** `CSC-BZU{DID_YOU_PLAY_FAIR}`
