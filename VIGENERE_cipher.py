import keyword


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

    
keyword = input("Enter keyword: ")  
text = input("Enter message: ")
print(encrypt(text, keyword.upper()))