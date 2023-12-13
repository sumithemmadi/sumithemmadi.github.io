import nltk
from nltk.corpus import stopwords

nltk.download("punkt")

english_frequencies = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0, 'f': 2.2,
    'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0,
    'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0,
    's': 6.3, 't': 9.1, 'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15,
    'y': 2.0, 'z': 0.074
}

nltk.download("punkt")


def caesar_cipher(text, shift, encrypt=True):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            shifted = ord(char) + shift_amount

            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26

            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift

            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26

            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


def frequency_analysis(encrypted_text):
    letter_count = {}
    total_letters = 0

    for char in encrypted_text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1

    frequencies = {}
    for char, count in letter_count.items():
        frequencies[char] = (count / total_letters) * 100

    sorted_letters = sorted(frequencies.items(),
                            key=lambda x: x[1], reverse=True)

    most_frequent_letter = sorted_letters[0][0]
    shift = (ord(most_frequent_letter) - ord('e')) % 26

    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(
        f"Decryption with Most Frequent Letter '{most_frequent_letter}' (Shift {shift}):")
    print(decrypted_text)


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Brute force decryption")
        print("4. Frequency analysis decryption")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            encrypt_file()
        elif choice == '2':
            decrypt_file()
        elif choice == '3':
            brute_force_decrypt()
        elif choice == '4':
            frequency_analysis_decrypt()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def encrypt_file():
    plaintext_filename = input("Enter the input file name: ")
    shift = int(input("Enter the shift value: "))

    with open(plaintext_filename, 'r') as f:
        plaintext = f.read()

    encrypted_text = caesar_cipher(plaintext, shift)

    encrypted_filename = input("Enter the encrypted file name: ")
    with open(encrypted_filename, 'w') as f:
        f.write(encrypted_text)


def decrypt_file():
    filename = input("Enter the encrypted file name: ")
    shift = int(input("Enter the shift value: "))

    with open(filename, 'r') as f:
        encrypted_text = f.read()

    decrypted_text = caesar_decrypt(encrypted_text, shift)

    decrypted_filename = input("Enter the decrypted file name: ")
    with open(decrypted_filename, 'w') as f:
        f.write(decrypted_text)


def brute_force_decrypt():
    encrypted_filename = input("Enter the encrypted file name : ")

    with open(encrypted_filename, 'r') as f:
        encrypted_text = f.read()

    biggest_numbers_location = 0

    stop_words = set(stopwords.words('english'))

    temp = 0
    shift_found1 = 0
    decrypted_text1 = ""
    stop_words_count1 = 0

    for shift in range(26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        words = nltk.word_tokenize(decrypted_text)
        stop_words_count = sum(
            1 for word in words if word.lower() in stop_words)

        if (stop_words_count >= temp):
            temp = stop_words_count
            shift_found1 = shift
            decrypted_text1 = decrypted_text
            stop_words_count1 = stop_words_count

    print(
        f"\nShift : {shift_found1:2} \n\nDecrypted Text : {decrypted_text1} \n\nNumber of stopwords : {stop_words_count1}")


def frequency_analysis_decrypt():
    filename = input("Enter the encrypted file name: ")

    with open(filename, 'r') as f:
        encrypted_text = f.read()

    frequency_analysis(encrypted_text)


main_menu()
