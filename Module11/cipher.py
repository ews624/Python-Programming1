
def encrypt(message):
    encrypted_message = ""

    for letter in message:
        try:
            encrypted_letter = cipher[letter]
            encrypted_message += encrypted_letter
        except:
            encrypted_message += letter

    return encrypted_message

def decrypt(message):
    decrypted_message = ''
    
    for letter in message:
        try:
            decrypted_letter = list(cipher.keys())[list(cipher.values()).index(letter)]
            decrypted_message += decrypted_letter
        except:
            decrypted_message += letter

    return decrypted_message
  
cipher = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9',
    'k': '!',
    'l': '@',
    'm': '#',
    'n': '$',
    'o': '%',
    'p': '^',
    'q': '&',
    'r': '*',
    's': '(',
    't': ')',
    'u': '-',
    'v': '+',
    'w': '<',
    'x': '>',
    'y': '?',
    'z': '='
}

print("Welcome to the Secret Message Encoder/Decoder")
print("1. Encode")
print("2. Decode a message")
print("3. Exit\n")

while True:

    choice = int(input("What would you like to do?"))

    if choice == 1:
        message = input("Enter a message to encode: ")
        encrypted_message = encrypt(message)
        print("Encoded message:", encrypted_message)        
    elif choice == 2:
        message = input("Enter a message to decode: ")
        decrypted_message = decrypt(message)
        print("Decoded message:", decrypted_message)
    elif choice == 3:
        break
    else:
        print(str(choice) + " is not a valid choice")
        
    
    
