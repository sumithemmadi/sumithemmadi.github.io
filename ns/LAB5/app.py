def c_encrypt(plaintext, key):
    key_length = len(key)
    cipher_columns = [''] * key_length

    for i in range(len(plaintext)):
        cipher_columns[i % key_length] += plaintext[i]

    cipher = ''.join(cipher_columns)
    return cipher

def c_decrypt(cipher, key):
    key_length = len(key)
    column_length = len(cipher) // key_length
    plaintext_columns = [''] * key_length

    for i in range(key_length):
        plaintext_columns[i] = cipher[i * column_length:(i + 1) * column_length]

    plaintext = ''
    for i in range(column_length):
        for j in range(key_length):
            plaintext += plaintext_columns[j][i]

    return plaintext

def main():
    while True:
        print("\nColumnar Transposition cipher")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            plaintext_filename = "plaintext.txt"
            encrypted_filename = "cipher.txt"
            key = input("Enter the encryption key: ")

            try:
                with open(plaintext_filename, 'r') as file:
                    plaintext = file.read()
                encrypted_text = c_encrypt(plaintext, key)

                with open(encrypted_filename, 'w') as file:
                    file.write(encrypted_text)

                print(f"Encryption completed. Encrypted text saved to {encrypted_filename}")
            except FileNotFoundError:
                print(f"File '{plaintext_filename}' not found.")

        elif choice == 2:
            encrypted_filename = "cipher.txt"
            decrypted_filename = "recover.txt"
            key = input("Enter the decryption key: ")

            try:
                with open(encrypted_filename, 'r') as file:
                    encrypted_text = file.read()
                decrypted_text = c_decrypt(encrypted_text, key)

                with open(decrypted_filename, 'w') as file:
                    file.write(decrypted_text)

                print(f"Decryption completed. Decrypted text saved to {decrypted_filename}")
            except FileNotFoundError:
                print(f"File '{encrypted_filename}' not found.")

        elif choice == 3:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
