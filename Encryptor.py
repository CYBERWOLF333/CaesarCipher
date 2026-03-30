import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
import pickle
import secrets
import string
import os

def encrypt_file(filepath, key):
    key = key.encode()
    with open(filepath, "rb") as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext, tag

def encrypt_clicked():
    key = key_entry.get()
    nonce, encrypted, tag = encrypt_file(selected_file, key)
    
    # Get the original extension to save it
    _, ext = os.path.splitext(selected_file)
    
    with open("encrypted.bin", "wb") as file:
        pickle.dump((nonce, encrypted, tag, ext), file)
    
    file_label.config(text="File encrypted and saved as encrypted.bin!")

def key_clicked():
    key = ""
    for i in range(16):
        key += secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

window = tk.Tk()
window.title("File Encryptor")
window.geometry("400x300")
selected_file = ""

def browse_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text="Selected File: " + selected_file)

file_label = tk.Label(window, text="Selected File:")
file_label.pack()

key_label = tk.Label(window, text="Key: ")
key_label.pack()

key_entry = tk.Entry(window, width=20)
key_entry.pack()

tk.Button(window, text="Browse File", command=browse_file).pack()
tk.Button(window, text="Generate Key", command=key_clicked).pack()
tk.Button(window, text="Encrypt File", command=encrypt_clicked).pack()

window.mainloop()
