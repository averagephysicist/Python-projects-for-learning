alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to Julio Cesar's army ")
choice = input("Would you like to encrypt or decrypt \n").lower()

def encrypt():
    message = input("type here your message:")
    shift = int(input("Type in the shift number:"))
    encrypted_message = " "

    for letter in message:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift)%26
            encrypted_message += alphabet[new_index]
            #keep spaces and punctuation unchanged    
        else:
            encrypted_message += letter  
    print(encrypted_message)

def unencrypt():
    message = input("Type in the encrypted message")
    shift = int(input("Type in the shift number:"))

    unencrypted_message = " "

    for letter in message:
        if letter in alphabet:
            original_index = (alphabet.index(letter) - shift)%26
            unencrypted_message += alphabet[original_index]
        else: unencrypted_message += letter    
    print(unencrypted_message)



if choice == "encrypt":
    encrypt()
elif choice == "decrypt":
    unencrypt()
else: 
    print("Please type in a valid choice")



   



