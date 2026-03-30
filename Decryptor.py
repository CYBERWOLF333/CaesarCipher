import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
import pickle
import os

def decrypt_file(encrypted, nonce, tag, key):
    key = key.encode()
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(encrypted, tag)
    return decrypted

def browse_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text="Selected: " + os.path.basename(selected_file))

def decrypt_clicked():
    key = key_entry.get()
    with open(selected_file, "rb") as file:
        nonce, encrypted, tag, ext = pickle.load(file)
    
    decrypted = decrypt_file(encrypted, nonce, tag, key)
    
    output_path = "decrypted_result" + ext
    with open(output_path, "wb") as file:
        file.write(decrypted)
    
    file_label.config(text="Decrypted and saved as: " + output_path)

window = tk.Tk()
window.title("File Decryptor")
window.geometry("400x300")
selected_file = ""

file_label = tk.Label(window, text="Selected File:")
file_label.pack()

key_label = tk.Label(window, text="Key: ")
key_label.pack()

key_entry = tk.Entry(window, width=20)
key_entry.pack()

button = tk.Button(window, text="Browse File", command=browse_file)
button.pack()

decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_clicked)
decrypt_button.pack()

window.mainloop()