
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

shift=int(input("what is your shift: "))

with open("message.txt", "r") as file:
    content = file.read()

encrypted = encrypt(content, shift)
#print("encrypted text:", encrypted)  # check this prints

with open("encrypted2.txt", "w") as file:
    file.write(encrypted)



