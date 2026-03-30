import tkinter as tk

def encrypt_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += encrypt_char(char, shift)
        else:
            result += char
    return result

def decrypt_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += decrypt_char(char, shift)
        else:
            result += char
    return result

def encrypt_clicked():
    text = entry.get()
    shift = int(shift_entry.get())          # get whatever the shift
    output_label.config(text=encrypt(text, shift))     # show it on the label
        
    
def decrypt_clicked():
    text = decrypt_entry.get()
    shift = int(shift_entry.get())          # get whatever the shift
    output2_label.config(text=decrypt(text, shift))     # show it on the label
    
    

window = tk.Tk()                        # create the window
window.title("My First GUI")            # give it a title
window.geometry("400x300")             # set the size (width x height)

label = tk.Label(window, text="Input your message and your shift!") # create a label
label.pack()                            # add it to the window

message_label = tk.Label(window, text="Message:") # create a label for message
message_label.pack()                            # add it to the window
entry = tk.Entry(window, width=30)  # text input box
entry.pack()

shift_label = tk.Label(window, text="Shift:") # create a label for shift
shift_label.pack()
shift_entry = tk.Entry(window, width=30)  # text input box for shift
shift_entry.pack()

encrypt_label = tk.Label(window, text="Encrypted Text:") # create a label for shift
encrypt_label.pack()

output_label = tk.Label(window, text="") # create a label for output
output_label.pack()

decrypt_label = tk.Label(window, text="Input Encrypted Text:") # create a label for shift
decrypt_label.pack()
decrypt_entry = tk.Entry(window, width=30)  # text input box
decrypt_entry.pack()

decryption_label = tk.Label(window, text="Decrypted Text:") # create a label for shift
decryption_label.pack()


output2_label = tk.Label(window, text="") # create a label for output
output2_label.pack()


button = tk.Button(window, text="Encrypt!", command=encrypt_clicked)
button.pack()

button = tk.Button(window, text="Decrypt!", command=decrypt_clicked)
button.pack()

window.mainloop()                       # keep the window open
