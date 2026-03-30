import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
import pickle
import secrets
import string
import os 


def encrypt_file(filepath, key):
    key = key.encode()
    with open(filepath, "rb") as file:    # rb = read bytes
        data = file.read()                 # data is already bytes!
    cipher = AES.new(key, AES.MODE_EAX)
    encrypted, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, encrypted

def encrypt_clicked():
    key = key_entry.get()
    nonce, encrypted = encrypt_file(selected_file, key)
    with open("encrypted.bin", "wb") as file:
        pickle.dump((nonce, encrypted), file)
    file_label.config(text="File encrypted and saved!")  # show success message
 


def decrypt_clicked():
    key = key_entry.get()
    with open("encrypted.bin", "rb") as file:
        nonce, encrypted = pickle.load(file)
    decrypted = decrypt_file(encrypted, nonce, key)
    
    # get the original file extension
    _, ext = os.path.splitext(selected_file)
    output_path = "decrypted_output" + ext  # e.g. decrypted_output.pdf
    
    with open(output_path, "wb") as file:
        file.write(decrypted)
    file_label.config(text="Decrypted and saved as: " + output_path)

def decrypt_file(encrypted, nonce, key):
    key = key.encode()
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt(encrypted)
    return decrypted                       # return raw bytes, not string!

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
    file_label.config(text="Selected File: " + selected_file)  # opens file browser

file_label = tk.Label(window, text="Selected File:") # create a label
file_label.pack()   

key_label = tk.Label(window, text="Key: ") # create a label
key_label.pack()       

key_entry = tk.Entry(window, width=20)
key_entry.pack()

button = tk.Button(window, text="Browse File", command=browse_file)
button.pack()


button = tk.Button(window, text="Generate Key", command=key_clicked)
button.pack()

encrypt_button = tk.Button(window, text="Encrypt File", command=encrypt_clicked)
encrypt_button.pack()


decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_clicked)
decrypt_button.pack()

window.mainloop()

