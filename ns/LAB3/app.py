from encrypt import encrypt_text
from decrypt import decrypt_text


while True:
    print("Menu:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '3':
        print("Exiting the program.")
        break

    if choice == '1':
        encrypt_text()
        print("Encryption completed. Ciphertext saved to 'ciphertext.txt'.")
    elif choice == '2':
        decrypt_text()
        print("Decryption completed. Recovered plaintext saved to 'recover.txt'.")

    else:
        print("Invalid input. Please select a valid option (1/2/3).")
