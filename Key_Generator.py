import secrets
import string

key = ""
for i in range(16):
    key += secrets.choice(string.ascii_letters + string.digits + string.punctuation)

print("Generated key:", key)