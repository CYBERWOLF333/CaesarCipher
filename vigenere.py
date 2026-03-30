def encrypt_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

def encrypt(text, keyword):
    result = ""
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[i]) - ord('A')
            i = (i + 1 ) % len(keyword)# encrypt char using shift
            result += encrypt_char(char, shift)# move i forward
        else:
            result += char
    return result

def decrypt_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

def decrypt(text, keyword):
    result = ""
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[i]) - ord('A')
            i = (i + 1 ) % len(keyword)# encrypt char using shift
            result += decrypt_char(char, shift)# move i forward
        else:
            result += char
    return result


choice = int(input("do you want to encrypt=1 or decrypt=2: "))
if choice == 1:
    keyword = input("Enter keyword: ")

    text = input("Enter message: ")

    encrypted = (encrypt(text, keyword.upper()))
    print("encrypted text:", encrypted)  # check this prints
    with open("encrypted.txt", "w") as file:
        file.write(encrypted)
    print("saved!")  #
elif choice == 2:
    keyword = input("Enter keyword: ")


    with open("encrypted.txt", "r") as file:
        content = file.read()
        decrypted = (decrypt(content, keyword.upper()))
        
        with open("decrypted.txt", "w") as file:
            file.write(decrypted)

else:
    print("invalid choice")




#with open("messages.txt", "r") as file:
 #   content = file.read()

#with open("encrypted.txt", "w") as file:
 #   file.write("test output")