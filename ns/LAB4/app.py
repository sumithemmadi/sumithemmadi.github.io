def RFE(text, key):

    rail = [['\n' for i in range(len(text))]
            for j in range(key)]
    print(len(rail))

    x = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            x = not x
        rail[row][col] = text[i]
        col += 1
        if x:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ("" . join(result))


def RFD(cipher, key):

    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    x = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            x = True
        if row == key - 1:
            x = False

        rail[row][col] = '*'
        col += 1

        if x:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        if row == 0:
            x = True
        if row == key-1:
            x = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if x:
            row += 1
        else:
            row -= 1
    return ("".join(result))


def main():
    while True:
        print("\nRail Fence Cipher Menu:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_file = input(
                "Enter the input file name (plaintext.txt): ") or "plaintext.txt"
            key = int(input("Enter the key value: "))
            with open(input_file, 'r') as file:
                plaintext = file.read()
            encrypted_text = RFE(plaintext, key)
            output_file = input(
                "Enter the output file name (cipher.txt): ") or "cipher.txt"
            with open(output_file, 'w') as file:
                file.write(encrypted_text)
            print("Encryption completed. Encrypted text saved to", output_file)

        elif choice == '2':
            input_file = input(
                "Enter the input file name (cipher.txt): ") or "cipher.txt"
            key = int(input("Enter the key value: "))
            with open(input_file, 'r') as file:
                ciphertext = file.read()
            decrypted_text = RFD(ciphertext, key)
            output_file = input(
                "Enter the output file name (recover.txt): ") or "recover.txt"
            with open(output_file, 'w') as file:
                file.write(decrypted_text)
            print("Decryption completed. Decrypted text saved to", output_file)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
