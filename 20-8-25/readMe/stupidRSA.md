# 🧮 Stupid RSA

## 🧩 Given Information
- **Hint 1:** The plaintext was padded so that `(M^e)` is just barely larger than `N`.
- **N:** Provided by the server
- **e:** Provided by the server
- **C:** Provided by the server

---

## 🤔 Step 1: Understand the Attack
Since `e = 3` and the ciphertext is very close to a perfect cube (just slightly larger than `N`),  
we can try to solve by computing successive cube roots of `(C + iN)` until we recover the message.

This is known as the **Low Exponent RSA (e=3) + Padding Attack**.

---

## 🔑 Step 2: Run the Solver Code

Use the [RSA solver script](../content/rsa_ctf_solver.py) to recover the plaintext.

- ✅ **Final Flag:** `CSC-BZU{i_w1ll_m@k3_3_l4rg3_1n_s3c0nd_t1m3}`


### Example Inputs from Server:

```bash
$ nc 165.227.48.186 96

N = 166414419851748788989257713862437433837353807003112730132800587353118934044036427655260761126183868499768443951057175141504432197881166018455352092934352227434366567495582820268349336572741055350875755841547956726307943920168258154837411697859871332799402593204671248512036432064942714368581129044315872096939

e = 3

C = 5012657100303855710425881933116963759695114067222431937135931013912354957881243918149438296134100675616736666939776081509903825791996155965807136997539644451459669432461270191479471912717744926637622716311758704967078162702691772019798362579846450334950181144783611252286794588568517717176804035264246673678
```
### [Code of server](../content/serverRSA.py)