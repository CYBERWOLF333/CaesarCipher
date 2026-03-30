
def encrypt_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
shift=int(input("what is your shift: "))

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


with open("messages.txt", "r") as file:
    content = file.read()
encrypted = encrypt(content, shift)

with open("encrypted.txt", "w") as file:
    file.write(encrypted)
    


with open("encrypted.txt", "r") as file:
    content = file.read()
decrypted = decrypt(content, shift)

with open("decrypted.txt", "w") as file:
    file.write(decrypted)
