from Crypto.Cipher import AES
import pickle
import secrets
import string

def encrypt(message, key):
    key = key.encode()                    # convert key to bytes
    message = message.encode()            # convert message to bytes
    cipher = AES.new(key, AES.MODE_EAX)  # create AES cipher
    encrypted, tag = cipher.encrypt_and_digest(message)
    return cipher.nonce, encrypted        # return nonce + encrypted bytes

def decrypt(encrypted, nonce, key):
    key = key.encode()                           # convert key to bytes
    cipher = AES.new(key, AES.MODE_EAX, nonce)  # recreate the safe with the nonce
    decrypted = cipher.decrypt(encrypted)        # unlock it
    return decrypted.decode()    # convert bytes back to string


choice = int(input("do you want to encrypt=1 or decrypt=2: "))
key = ""
for i in range(16):
        key += secrets.choice(string.ascii_letters + string.digits + string.punctuation)
print("Your message has been encrypted")        
print("Generated key:", key)
print("keep it safe!")


if choice == 1:
    #key = input("Enter a 16 character key: ")
    #message = input("Enter message: ")
   

    with open("message.txt", "r") as file:
        message = file.read()
    
    if len(key) != 16:
        print("Key must be exactly 16 characters!")
    else:
        nonce, encrypted = encrypt(message, key)      # call encrypt with what arguments?
        with open("encrypted.bin", "wb") as file:
            pickle.dump((nonce, encrypted), file)         # what two things are we saving?
        print("saved!")

elif choice == 2:
    key = input("Enter a 16 character key: ")
    
    with open("encrypted.bin", "rb") as file:
        nonce, encrypted = pickle.load(file)     # what are we loading from?
    
    decrypted = decrypt(encrypted, nonce, key)
    with open("decrypted.txt", "w")as file:
        file.write(decrypted)             # what three things does decrypt need?
    #print("decrypted:", decrypted)

else:
    print("invalid choice")

