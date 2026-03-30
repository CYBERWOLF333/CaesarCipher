# 🔐 Python Encryption Projects

A collection of encryption tools built in Python, ranging from classic ciphers to real AES encryption. Built from scratch as a learning project.

---

## 📁 Projects Overview

| File | Description |
|---|---|
| `TEXT_FILE_ENCRYPTOR.py` | Encrypts a text file using the Caesar cipher |
| `VIGENERE_cipher.py` | Vigenere cipher encryption and decryption (no GUI) |
| `vigenere.py` | Alternative Vigenere cipher implementation |
| `AES_ENCRYPTION.py` | AES encryption and decryption in the terminal |
| `AES_GUI.py` | Full AES file encryptor and decryptor with a GUI |
| `Encryptor.py` | GUI app that encrypts any file with an auto-generated key |
| `Decryptor.py` | GUI app that decrypts a file using a key and encrypted file |
| `Key_Generator.py` | Generates a random secure 16-character AES key |

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- pycryptodome library

### Install dependencies
```
pip install pycryptodome
```

---

## 📖 How to Use Each File

### TEXT_FILE_ENCRYPTOR.py
Encrypts the contents of a text file using the Caesar cipher and saves the result to `encrypted2.txt`.

1. Create a file called `message.txt` in the same folder and add your text
2. Run the script
3. Enter your shift number when prompted
4. Check `encrypted2.txt` for the encrypted output

```
python TEXT_FILE_ENCRYPTOR.py
```

---

### VIGENERE_cipher.py / vigenere.py
Encrypts and decrypts text using the Vigenere cipher — a more secure version of the Caesar cipher that uses a keyword instead of a single shift number.

1. Run the script
2. Choose encrypt (1) or decrypt (2)
3. Enter your keyword
4. Enter your message
5. The encrypted/decrypted result will be saved to a file

```
python VIGENERE_cipher.py
```

---

### AES_ENCRYPTION.py
Terminal based AES encryption and decryption. Uses real AES-EAX encryption — the same standard used by banks and governments.

1. Run the script
2. Enter a exactly 16 character key
3. Enter your message
4. The script encrypts then immediately decrypts to verify it works

```
python AES_ENCRYPTION.py
```

---

### AES_GUI.py
A full GUI application for encrypting and decrypting any file (PDFs, images, text files) using AES encryption.

1. Run the script — a window will open
2. Click **Browse File** to select any file
3. Either type a 16 character key or click **Generate Key** for a random one
4. Click **Encrypt File** — saves encrypted data to `encrypted.bin`
5. To decrypt, make sure the key is the same, then click **Decrypt File**
6. The decrypted file is saved with its original extension (e.g. `decrypted_output.pdf`)

```
python AES_GUI.py
```

> ⚠️ Save your key somewhere safe — without it you cannot decrypt your file!

---

### Encryptor.py
A simple GUI app that encrypts any file with an automatically generated secure key.

1. Run the script — a window will open
2. Click **Browse File** to select the file you want to encrypt
3. Click **Generate Key** — a secure random key will appear
4. Copy and save your key somewhere safe
5. Click **Encrypt** — your file is encrypted and saved

```
python Encryptor.py
```

---

### Decryptor.py
A GUI app for decrypting files that were encrypted with the Encryptor or AES_GUI.

1. Run the script — a window will open
2. Click **Browse File** to select your encrypted file
3. Enter the key that was used to encrypt it
4. Click **Decrypt** — your original file is restored

```
python Decryptor.py
```

---

### Key_Generator.py
Generates a random secure 16 character key for use with AES encryption.

1. Run the script
2. A random key is printed — copy and save it

```
python Key_Generator.py
```

---

## 🔑 Important Notes

- AES keys must be **exactly 16 characters** long
- Always save your key — there is no way to recover encrypted files without it
- The Vigenere keyword can be any length and any letters
- Caesar cipher shift numbers can be any whole number

---

## 🧠 What I Learned Building This

- How classical ciphers work (Caesar, Vigenere)
- ASCII values and how `ord()` and `chr()` work in Python
- Real AES encryption using the `pycryptodome` library
- Reading and writing files in Python including binary files
- Building GUI applications with `tkinter`
- Generating cryptographically secure random keys with `secrets`

---

## 📚 Built With

- Python 3
- [pycryptodome](https://pycryptodome.readthedocs.io/)
- tkinter (built into Python)
