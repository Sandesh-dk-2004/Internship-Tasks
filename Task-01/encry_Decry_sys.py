def encryption(message, key):
    encrypted=""
    for char in message:
        if char.isalpha():
            shift =65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted

def decryption(encrypted_message, key):
    decrypted=""
    for char in encrypted_message:
        if char.isalpha():
            shift =65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted += char
    return decrypted

message=input("Enter the message for encryption : ")
key=int(input("Enter the key value : "))

encrypted_message=encryption(message,key)
print("Encrypted message is : ",encrypted_message)

dencrypted_message=decryption(encrypted_message,key)
print("Decrypted message is : ",dencrypted_message)