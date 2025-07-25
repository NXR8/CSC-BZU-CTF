# 🧮 Hill To Hell

## 🧩 Given Information:

- **Block Size:** 2
- **Encryption Formula:** `C = K × P mod 26`
- **E("HELP") = BJUP**
- **Encrypted Flag:** `YUX-AFF{PDGV_CWSRBK_OIC_GN_UOVD}`

---

## 🔍 Step 1: Derive the Key Matrix
![Step 1](../image/S1HillToHell.png)

🔗 You can use [DCode - Matrix Inverse](https://www.dcode.fr/matrix-inverse)
---

## 🔐 Step 2: Decrypt the Encrypted Flag

Use the key `NXRS` with a Hill Cipher decryption tool:

🔗 You can use [DCode - Hill Cipher Tool](https://www.dcode.fr/hill-cipher)

**Decrypted Result:**  
`CSC-BZU{HILL_CIPHER_KEY_IS_NXRY}`

⚠️ *Note: The tool might pad the plaintext with an "A" if needed, which can slightly change the output.*

### ✅ Final Corrected Flag:
```

CSC-BZU{HILL_CIPHER_KEY_IS_NXRS}

```

---

![Insert Matrix Inverse or Decryption Screenshot](../image/HillToHell.png)
